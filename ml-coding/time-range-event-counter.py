from collections import defaultdict
from typing import List, Tuple

class EventCounter:
    """
    Counts events in arbitrary time windows. Handles out-of-order insertions.
    Uses sorted list + binary search for O(log n) queries.

    Insert: O(n) worst case (insort shifts elements)
    Query: O(log n)
    Eviction: O(idx) — removes stale events to bound memory.

    Large-scale alternative: bucket counts by minute → O(1) insert/query,
    bounded memory, slight loss of precision.
    """

    def __init__(self):
        self.timestamps: List[float] = []  # Always sorted

    def _bisect_right(self, val: float) -> int:
        """Return index where val should be inserted to keep list sorted (right of equals)."""
        l, r = 0, len(self.timestamps) - 1
        res = len(self.timestamps)
        while l <= r:
            m = (l + r) // 2
            if self.timestamps[m] > val:
                res = m
                r = m -1
            else:
                l = m +1
        return res

    def _bisect_left(self, val: float) -> int:
        """Return index of leftmost position where val could be inserted."""
        l, r = 0, len(self.timestamps) - 1
        res = len(self.timestamps) 
        while l <= r:
            m = (l + r) // 2
            if self.timestamps[m] >= val:
                res = m
                r = m -1
            else:
                l = m + 1
        return res

    def add_event(self, timestamp: float):
        """Insert in sorted order using binary search. Handles out-of-order. O(n) due to list shift."""
        idx = self._bisect_right(timestamp)
        self.timestamps.insert(idx, timestamp)
         # built-in: bisect.insort(self.timestamps, timestamp)

    def count_in_window(self, start: float, end: float) -> int:
        """Count events in [start, end] inclusive. O(log n)."""
        if start > end:
            return 0
        left = self._bisect_left(start)
        right = self._bisect_right(end)
        # built-in: left  = bisect.bisect_left(self.timestamps, start)
        # built-in: right = bisect.bisect_right(self.timestamps, end)
        return right - left

    def count_last_n_seconds(self, current_time: float, window_secs: float) -> int:
        """Count events in rolling window [current - window, current]."""
        """
        use cases:
        "how many times did this user watch something in the last 30 minutes" or 
        "how many ad clicks happened in the last 5 minutes." 
        Those are rolling window queries, not fixed absolute window queries.

        """
        return self.count_in_window(current_time - window_secs, current_time)

    def evict_before(self, cutoff: float):
        """Remove events older than cutoff. Bounds memory for streaming use cases."""
        idx = self._bisect_left(cutoff)
        del self.timestamps[:idx]  # O(n) but amortized acceptable

    def total_count(self) -> int:
        return len(self.timestamps)


class BucketedEventCounter:
    """
    Approximate counter using time buckets.
    
    Insert: time O(1)
    Query: time O(W / bucket_size) 

    Space: O(W/bucket_size). W = full time range 
    
    Trade-off: precision lost within a bucket window.
    Smaller bucket_size = more precision, more memory, slower query.
    Larger bucket_size  = less precision, less memory, faster query.

    Better for millions of events per second.


    """

    def __init__(self, bucket_size: float = 1.0):
        self.bucket_size = bucket_size
        self.buckets: dict = defaultdict(int)  # bucket_key -> event count

    def add_event(self, timestamp: float):
        """Increment the count for the bucket this timestamp falls into. O(1)."""
        bucket_key = int(timestamp // self.bucket_size)
        self.buckets[bucket_key] += 1

    def count_in_window(self, start: float, end: float) -> int:
        """
        Sum counts across all buckets that overlap [start, end].
        This is approximate: boundary buckets may include events
        outside the exact requested window.
        O(W/bucket_size) where W = end - start.
        """
        if start > end:
            return 0
        start_bucket = int(start // self.bucket_size)
        end_bucket = int(end // self.bucket_size)
        return sum(self.buckets[b] for b in range(start_bucket, end_bucket + 1))

    def count_last_n_seconds(self, current_time: float, window_secs: float) -> int:
        """Count events in the rolling window [current_time - window_secs, current_time]."""
        return self.count_in_window(current_time - window_secs, current_time)

    def total_count(self) -> int:
        return sum(self.buckets.values())




# ─── TEST CASES ─────────────────────────────────────────────────────────
def test_event_counter():
    ec = EventCounter()

    # Normal case: in-order events
    for t in [1, 2, 3, 4, 5]:
        ec.add_event(t)
    assert ec.count_in_window(2, 4) == 3

    # Out-of-order insertion
    ec2 = EventCounter()
    for t in [5, 1, 8, 3, 7, 2]:
        ec2.add_event(t)
    assert ec2.timestamps == [1, 2, 3, 5, 7, 8] # Must stay sorted
    assert ec2.count_in_window(2, 6) == 3   # 2, 3, 5
    assert ec2.count_last_n_seconds(8, 5) == 3  # 3,5,7,8 → 4 events in [3,8]

    # Edge case: empty window
    assert ec2.count_in_window(10, 20) == 0

    # Edge case: start > end
    assert ec2.count_in_window(5, 2) == 0

    # Edge case: single event exactly at boundary
    assert ec2.count_in_window(7, 7) == 1

    # Eviction
    ec2.evict_before(4)
    assert ec2.timestamps == [5, 7, 8] # Events < 4 should be removed

    # Duplicate timestamps
    ec3 = EventCounter()
    ec3.add_event(1.0)
    ec3.add_event(1.0)
    ec3.add_event(1.0)
    assert ec3.count_in_window(1.0, 1.0) == 3

    print("All EventCounter tests passed")

test_event_counter()



def test_bucketed_event_counter():

    # Normal case: events fall cleanly inside buckets, no boundary ambiguity
    # bucket_size=1.0, so timestamp 1.0, 2.0, 3.0 each go to bucket 1, 2, 3
    bc = BucketedEventCounter(bucket_size=1.0)
    bc.add_event(1.0)
    bc.add_event(2.0)
    bc.add_event(3.0)
    bc.add_event(4.0)
    bc.add_event(5.0)
    assert bc.count_in_window(2.0, 4.0) == 3   # buckets 2, 3, 4
    assert bc.count_in_window(1.0, 5.0) == 5   # all events

    # Multiple events in the same bucket
    bc2 = BucketedEventCounter(bucket_size=1.0)
    bc2.add_event(1.1)
    bc2.add_event(1.5)
    bc2.add_event(1.9)   # all three go to bucket 1
    bc2.add_event(2.2)   # goes to bucket 2
    assert bc2.count_in_window(1.0, 1.0) == 3  # bucket 1 has all three
    assert bc2.count_in_window(2.0, 2.0) == 1  # bucket 2 has one

    # *Precision loss demo: boundary buckets include events outside the exact window
    # Query is [1.5, 2.5] but bucket 1 includes 1.1 and 1.9 too
    # So we expect 4 (all events) even though exact window would give 2
    bc3 = BucketedEventCounter(bucket_size=1.0)
    bc3.add_event(1.1)   # bucket 1, outside [1.5, 2.5]
    bc3.add_event(1.8)   # bucket 1, inside [1.5, 2.5]
    bc3.add_event(2.2)   # bucket 2, inside [1.5, 2.5]
    bc3.add_event(2.9)   # bucket 2, outside [1.5, 2.5]
    # exact answer would be 2, but bucketed returns 4 (overcounts boundaries)
    assert bc3.count_in_window(1.5, 2.5) == 4  # known overcount

    # Smaller bucket reduces precision loss
    bc4 = BucketedEventCounter(bucket_size=0.1)
    bc4.add_event(1.1)   # bucket 11
    bc4.add_event(1.8)   # bucket 18
    bc4.add_event(2.2)   # bucket 22
    bc4.add_event(2.9)   # bucket 29
    # query [1.5, 2.5] covers buckets 15 to 25
    # only 1.8 (bucket 18) and 2.2 (bucket 22) fall in that range
    assert bc4.count_in_window(1.5, 2.5) == 2  # exact with small buckets

    # Rolling window
    bc5 = BucketedEventCounter(bucket_size=1.0)
    for t in [1.0, 2.0, 3.0, 8.0, 9.0]:
        bc5.add_event(t)
    assert bc5.count_last_n_seconds(current_time=9.0, window_secs=3.0) == 2  # 8, 9

    # Edge: empty counter
    bc6 = BucketedEventCounter(bucket_size=1.0)
    assert bc6.count_in_window(0.0, 10.0) == 0

    # Edge: start > end
    bc7 = BucketedEventCounter(bucket_size=1.0)
    bc7.add_event(2.0)
    assert bc7.count_in_window(5.0, 1.0) == 0

    # Total count
    bc8 = BucketedEventCounter(bucket_size=1.0)
    bc8.add_event(1.0)
    bc8.add_event(2.0)
    bc8.add_event(3.0)
    assert bc8.total_count() == 3

    print("All BucketedEventCounter tests passed")


test_bucketed_event_counter()

