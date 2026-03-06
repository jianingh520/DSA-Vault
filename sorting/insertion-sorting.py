class Solution:
    def insertionSort(self, nums):
        # Size of the array 
        n = len(nums)
        # For every element in the array 
        for i in range(1, n):
            # Current element as key 
            key = nums[i]
            j = i - 1
            # Shift elements that are greater than key by one position
            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            # Insert key at correct position
            nums[j+1] = key
        return nums
        # [7, 4, 1, 5, 3]
        #. j  i(key)
        #. 7  7, 1, 5, 3
        #  4, 7, 1, 5, 3
        #     j i(key)
        #  1  4  7  5. 3
        #        j   i(key)
        #  1  4  5   7. 3
        #            j  i(key) 
        #  1 3   4   5  7

# time O(n^2), space O(1)