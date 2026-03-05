class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # max_count 
        # counting 1 as we traverse the arr. if we encounter a 1, increse the counter. if we meet zero, reset the counter. at each step, we track the maximum streak length seen so far

        max_cnt = 0
        cur = 0
        for n in nums:
            if n == 1:
                cur += 1
            else:
                cur = 0
            max_cnt = max(max_cnt, cur)
        return max_cnt
        # time O(n), space O(1)

        