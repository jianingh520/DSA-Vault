class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # append remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result

# Time Complexity: O(N*logN), merging two arrays take linear time and array is recursively divided into halves (logN times).
# Space Complexity: O(N), we use a temporary array to store elements in sorted order.