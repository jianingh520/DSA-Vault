class Solution:
    def findPeakElement(self, nums):
        # naive: linear search. Time O(N), Space O(1)
        # optimized: binary search. Time O(logN), Space O(1)
        
        # edge cases:
            # nums[n-1] > nums[n-2] -> peak
            # nums[0] > nums[1] -> peak
        # case1: nums[m] > nums[m-1] and nums[m] > nums[m+1] -> peak
        # case2: nums[m] < nums[m+1], search right
        # case3: nums[m] >= nums[m+1], search left  

        n = len(nums)

        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        l, r = 1, n-2
        while l <= r:
            m = l + (r-l)//2
            # find peak
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            if nums[m] < nums[m+1]:
                # search right
                l = m + 1
            else:
                # search left
                r = m - 1
        return -1
            