class Solution:
    def rearrangeArray(self, nums):
        # two pass:
            # traverse arr, get all postive, and all negative
            # merge two arr into one, start with postive
            # time O(n), space O(n)

        # opt: one pass
            # pos_idx, neg_idx= 0, 1, traverse the nums, if n > 0, put it to res[pos_idx], pos_idx +=2
            #   else,  put it to res[neg_idx], neg_idx +=2
            # time O(n), space O(n)

        pos_idx, neg_idx = 0, 1
        res = [0]*len(nums)

        for n in nums:
            if n > 0:
                res[pos_idx] = n
                pos_idx += 2
            else:
                res[neg_idx] = n
                neg_idx +=2
        return res