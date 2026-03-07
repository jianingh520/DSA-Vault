class Solution:
    def search(self, nums, target):
        # rotated arr: even though the array is rotated, one half of the array must still be sorted.
        # clarify: 
            # are all elements unique?
            # if the target is not in the array, should i return -1?
         
        # naive: linear search O(n)
        # better: init l, r search range, 
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
                return m
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
        return -1
        # nums = [7, 8, 0, 1, 2, 4, 5], k = 0 -> return 2
            # l, r = 0, 6. m = 3
            # l, r = 0, 2. m = 1
            # l, r = 2, 2, m = 2 
        # nums = [4, 5, 6, 7, 0, 1, 2], k = 0 -> return 4
            # l, r = 0, 6. m = 3 
            # l, r = 4 ,6. m = 5
            # l, r = 4, 4. m = 4 

 
    
    
