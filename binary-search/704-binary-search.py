class Solution:
    def search(self, nums, target):
        # naive: linear search, traverse the arr and check if num==target.
            # time O(n), space O(1)
        # better: since the arr is sorted, use binary search. 
            # initailize l, r searching range, if target > num[mid], update r = m-1. elif update l = m+1, if target found, retrun
            # Time: O(log n), since binary search half searching space at each step. Space O(1)

        l, r = 0, len(nums)-1
        while l <= r: 
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1

        # edge case nums=[5], when l==r still valid

