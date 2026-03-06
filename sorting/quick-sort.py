class Solution:
    def quickSort(self, nums, low, high):
        if low < high:
            # Partition index
            pi = self.partition(nums, low, high)

            # Sort left half
            self.quick_sort(nums, low, pi - 1)

            # Sort right half
            self.quick_sort(nums, pi + 1, high)


    def partition(nums, low, high):
        pivot = nums[high]  # choose last element as pivot
        i = low - 1        # index of smaller element

        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        # place pivot in correct position
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1