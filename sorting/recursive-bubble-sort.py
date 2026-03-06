class Solution:
    def bubbleSort(self, nums, n):
        if n == 1:
            return 

        swapped = False
        for j in range(n-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        
        if not swapped:
            return 
        
        self.bubbleSort(nums, n-1)