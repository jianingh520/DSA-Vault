class Solution:
    def selectionSort(self, nums):
        
        for i in range(len(nums)):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_idex = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
    
        # O(n^2)

    # [7, 4, 1, 5, 3]
    #  i