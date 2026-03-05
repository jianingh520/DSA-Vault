class Solution:
    def longestSubarray(self, nums, k):
        # 1, use two pointer maintain the window to track sum inside the window. These pointers represent the start and end of the current subarray
        # the right pt to expand the window, if cur window sum > k, shrink window. if sum==k, update max_window size
        # time O(n), space O(1)
        # Subarray = continuous window
        # only works for positive

        n = len(nums)
        max_window = 0 # 2, 4
        cur_sum = 0
        l = 0
        for r in range(n): # r=0, 1 ,2, 3, 4
            cur_sum += nums[r] # 19 
            while cur_sum > k:
                cur_sum -= nums[l]
                l += 1
            if cur_sum == k:
                max_window = max(max_window, r - l + 1)
        return max_window

 