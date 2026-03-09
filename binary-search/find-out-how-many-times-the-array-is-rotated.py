class Solution:
    def findKRotation(self, nums):
        # naive: linear search O(n), sapce O(1)
        # better: find minimum in rotated array. the ans is the index of minimum
            # binary search O(logN), sapce O(1)
            # since the array is rotated, there is at least one side is sorted. the minimum lies around the pivot where the order break
            # init l, r search range,
                # case 1 nums[l] <= nums[r]: sorted, res = min(res, nums[l])
                # update res = min(res, nums[m])
                    # case 2 nums[m] > nums[r]: search right
                    # case 3 num[m] <= nums[r]: search left

        l, r = 0, len(nums) -1
        res = nums[0]
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break 
            m = l+(r-l)//2
            res = min(res, nums[m])
            if num[m] > nums[r]:
                l = m + 1 # search right
            else:
                # search left
                r = m -1
        return res
