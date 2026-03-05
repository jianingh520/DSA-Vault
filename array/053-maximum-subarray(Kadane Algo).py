class Solution:
    def maxSubArray(self, nums):
        # check every subarr O(n^3)
        # note: only use sliding window if we need the the length of subarr

        # maintain a cur_sum, max_sum, traverse the arr, at each step add new element,  if cur_sum>max_sum, update max_sum, if cur_sum < 0, reset the cur = 0; otherwise,
        # time: O(n), space O(1)

        #  nums = [2, 3, 5, -2, 7, -4]
        #  nums = [-2, -3, -7, -2, -10, -4]
        # cur 
        # max -2
        cur_sum = 0
        max_sum = float('-inf')

        # follow up: print that subarr
        start = 0
        res_start = 0
        res_end = 0

        for i, n in enumerate(nums):
            cur_sum += n
            if cur_sum > max_sum:
                max_sum = cur_sum
                # add this
                res_start = start
                res_end = i
            if cur_sum < 0:
                cur_sum = 0
                # add this
                start = i + 1
        return max_sum, nums[res_start: res_end +1]