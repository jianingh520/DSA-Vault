class Solution:
    def findMin(self, nums):
        # rotated sorted array: even though the array is rotated, one half of array must be sorted
        # clarify:
            # are all element unique?
            # can array be empty?
        # naive: linear search O(n)
        # better: binary search. 
            # even though the array is rotated, at least one part of the array still preserves sorted order. The minimum element lies around the pivot where the order breaks.
            # init l, r search range, update res=min (res,nums[m])
                # if nums[r] < nums[m] -> search right
                # otherwise, search left
            # case 1: nums[l] <= nums[r] -> already sorted, res = min(res, num[l])
            # case 2: nums[r] < nums[m] -> search right
            # case 3: nums[r] >= nums[m] -> search left

            #Time:O(logN), Space:O(n)

        
        l, r = 0, len(nums)-1
        res = nums[0]
        while l <= r:
            
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            m = l + (r-l)//2
            res = min(res, nums[m])

            if nums[m] > nums[r]:
                # search right
                l = m +1
            else:
                # search left
                r = m -1
        return res 

