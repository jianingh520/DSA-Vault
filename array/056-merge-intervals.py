class Solution:
    def mergeOverlap(self, intervals):
        # Your code goes here
        # intervals[i] = [start_i, end_i]
        # clarify: is the start_i sorted?
            #.     is end_i alwalys greater than start_i
            #.     can intervals be empty?
            #.     [0, 1], [1, 2] => [0,2]

        # naive: check every pair and then merge. time O(n^2)
        # better: sort array by start_i, and traverse the intervals, if cur_start < last_end, update last_end = max(cur_end, last_end). otherwise, add current intervals to the res
            # time: O(nlogn), output space:O(num of intervals)-> O(n), auxilary space O(1)
        
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            cur_start = intervals[i][0]
            last_end = res[-1][1]
            if cur_start <= last_end:
                res[-1][1] = max(last_end, intervals[i][1])
            else:
                res.append(intervals[i])
        return res

        # [[1, 5], [3, 6], [8, 10], [15, 18]]
            # res = [1, 6], [8, 10], [15, 18]
        # [[1,3],[4,6],[5,7],[8,10]]
            # res = [1, 3], [4, 6], [4, 7], [8,10]


