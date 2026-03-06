class Solution:
    def insertionSort(self, nums, i, n):
        # Base case
        if i == n:
            return

        j = i
        # Move the element to the left while it's smaller than its predecessor
        while j > 0 and arr[j - 1] > arr[j]:
            # Swap
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

        # Recur for the next index
        self.insertion_sort(arr, i + 1, n)      