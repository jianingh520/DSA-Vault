class Solution:
    def upperBound(self, nums, x):
        # upper bound: smallest index where nums[i] > x
        # if no such index is found, return the size of the array.

        # naive: linear search. time:O(n)
        # better: since array is sorted, we can apply binary search.
            # init l, r search range, if nums[m] > x, update res = m, search left 
            # otherwise, search right
            # time: O(logn), space:O(1)

        l, r = 0, len(nums)-1
        res = len(nums)
        while l <= r:
            m = l + (r-l) //2
            if nums[m] > x:
                res = m
                r = m - 1 # search left
            else:
                l = m + 1 # search right
        return res
