class Solution:
    def searchInARotatedSortedArrayII(self, nums, target):
        # rotated arr: even though the array is rotated, one half of the array must still be sorted.
        # clarify: 
            # are all elements unique?
            # if the target is not in the array, should i return -1?
            # can array be empty?
         
        # naive: linear search O(n)
        # better: init l, r search range, 
            # if target found, return True 
            # dedup: if nums[l] == nums[m] == nums[r]: l+=1, r-=1 continue the loop
            # if left part is sorted, check if target inside the left range, if yes, search left, else search right
                # nums[l] <= nums[m]
            # if right part is soeted, check if target inside the right range, if yes search right, else search left
                # nums[l] > nums[m]
                #  nums = [7, 8, 0, 1, 2, 4, 5], k = 0
            # time: O(logn), space O(1)

        l, r = 0, len(nums) -1
        while l <= r:
            m = l + (r-l) //2
            if nums[m] == target:
                return True
            
            # remove ambiguity caused by duplicates
            if nums[l] == nums[m] == nums[r]:
                l +=1
                r -=1
                continue
            # if left part sorted
            if nums[l] <= nums[m]:
                # check if target in range
                if nums[l] <= target < nums[m]:
                    # search left
                    r = m - 1
                else: 
                    # search right
                    l = m + 1
            # if right part sorted
            else:
                # check if target in right part
                if nums[m] < target <= nums[r]:
                    # search right
                    l = m + 1
                else:
                    # search left
                    r = m - 1
        return False


 
    
    
