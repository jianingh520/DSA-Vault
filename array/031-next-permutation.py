class Solution:
    def nextPermutation(self, nums):
        # Set index
        index = -1

        # Find decreasing point
        for i in range(len(nums) - 2, -1, -1):
            # If smaller found
            if nums[i] < nums[i + 1]:
                index = i
                break

        # If no such index
        if index == -1:
            # Reverse whole list
            nums.reverse()
            return

        # Find just greater element
        for i in range(len(nums) - 1, index, -1):
            if nums[i] > nums[index]:
                # Swap them
                nums[i], nums[index] = nums[index], nums[i]
                break

        # Reverse part after index
        nums[index + 1:] = reversed(nums[index + 1:])
