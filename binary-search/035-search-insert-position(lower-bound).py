class Solution:
    def searchInsert(self, nums, target):
        # the first index where nums[i] >= target -> lower bound
        # naive: linear search. time: O(n)
        # better: since arr is sorted, use binary search. 
            # init l, r search range, if nums[m] >= target, update res =m, search left
            # otherwise, seach right
            # time O(logn), space O(1)

        l, r = 0, len(nums)-1
        res = len(nums)
        while l <= r:
            m = l + (r-l)//2
            if nums[m] >= target:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res 
