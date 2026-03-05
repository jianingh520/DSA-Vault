class Solution:
    def longestSubarray(self, nums, k):
        # 1, use two pointer maintain the window to track sum inside the window. These pointers represent the start and end of the current subarray
        # the right pt to expand the window, if cur window sum > k, shrink window. if sum==k, update max_window size
        # time O(n), space O(1)
        # Subarray = continuous window
        # only works for positive

        # n = len(nums)
        # max_window = 0 # 2, 4
        # cur_sum = 0
        # l = 0
        # for r in range(n): # r=0, 1 ,2, 3, 4
        #     cur_sum += nums[r] # 19 
        #     while cur_sum > k:
        #         cur_sum -= nums[l]
        #         l += 1
        #     if cur_sum == k:
        #         max_window = max(max_window, r - l + 1)
        # return max_window

        # nums = [10, 5, 2, 7, 1, 9], k = 15
            # cur

        # 2. how about there are negative number in array, 
            # use prefix sum + hash map, 
                # hash map -> {prefix_sum: first index}

        prefix_sum = {0: -1}   # {prefix_sum: first index}
        cur_sum = 0
        best_length = 0
        for i, n in enumerate(nums):
            cur_sum += n
            diff = cur_sum - k 
            if diff in prefix_sum:
                best_length = max(best_length, i  - prefix_sum[diff])
            if cur_sum not in prefix_sum:
                prefix_sum[cur_sum] = i
        return best_length

