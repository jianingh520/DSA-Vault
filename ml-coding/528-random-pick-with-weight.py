# Weighted Random Sampling (LeetCode 528)

class WeightedSampler:
    """
    Weighted random sampling using prefix sum and binary search.

    Build: O(n)
    pick_one: O(log n)
    pick_k: O(k * n)
    Space: O(n)
    """

    def __init__(self, w: List[int]):
        # prefix sum, time and space O(n)
        self.weights = weights          # store original for pick_k
        self.prefix_sum = []
        cur_sum = 0
        for weight in w:
            cur_sum += weight
            self.prefix_sum.append(cur_sum)
        self.total = cur_sum
        self.n = len(self.prefix_sum)

    def pickIndex(self) -> int:
        # use binary search to find the first index where prefix_sum[m] >= target
        # time: O(logn)

        """
        Pick one index proportional to weight. O(log n).
        Uses random.random() which is [0, 1) to guarantee
        target is always strictly less than total.

        Find first index where cumulative[i] >= target.
        Binary search, O(log n).
        res starts at n as the "not found" sentinel.
        """

        target = self.total * random.random() # why [0,1) works?
        l, r = 0, self.n -1
        res = self.n
        while l <= r:
            m = l + (r-l)//2
            if self.prefix_sum[m] >= target:
                res = m
                # search left
                r = m-1
            else:
                # search right
                l = m +1
        return res

    def pick_k(self) -> List[int]:
    	"""
        Pick k distinct indices without replacement. O(k * n).
        Each round removes the chosen item from the pool and
        rebuilds the sampler on the remaining items.

        local_idx: position inside the shrinking pool (0 to remaining-1)
        global_idx: original index in the full weights array
        available_idx maps local to global.

        For large k, consider Fisher-Yates on weighted array.
    	"""
    	if k > self.n:
    		raise ValueError(f"k={k} exceeds number of items={self.n})")

    	available_idx = list(range(self.n))
        chosen = []

        for _ in range(k):
            # build sampler on remaining weights only
            tmp = WeightedSampler([self.weights[i] for i in available_idx])

            # local position inside the shrinking pool
            local_idx = tmp.pickIndex()

            # translate back to original index
            global_idx = available_idx[local_idx]

            chosen.append(global_idx)
            available_idx.pop(local_idx)    # shrink the pool

        return chosen


## test case
