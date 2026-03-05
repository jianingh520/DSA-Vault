class Solution:
    def missingNumber(self, nums):
        # put nums to set, and iterate 0-n and check which one missing
        # time, space O(n)
        # sum(0-n) - sum(nums). time O(n),  space O(1)

        n = len(nums)
        total_sum = sum(nums)
        expect_sum = (n * n+1) // 2
        return expect_sum - total_sum
        # time: O(n), space O(1)
