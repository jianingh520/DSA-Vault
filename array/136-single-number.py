class Solution:
    def singleNumber(self, nums):
        # your code goes here
        # hash map to store the frequency, iterate through items in the hash map to find the singleNumber
        # time O(n), space O(n)

        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        for k, v in freq.items():
            if v == 1:
                return k
        return -1
        