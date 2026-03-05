class Solution:
    def longestConsecutive(self, nums):
        # sorting
        # maintain max_seq, cur_seq while traversing the arr, if nums[i]+1 == nums[i-1], cur_seq+=1, update max_seq
            # else: cur_seq = 1
        
        # Time O(nlogn), Space O(n) due to sorting 
        # if not nums:
        #     return 0

        # nums.sort()
        # max_seq = 1
        # cur_seq = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i-1]:
        #         if nums[i] == nums[i-1] + 1:
        #             cur_seq += 1
        #             max_seq = max(max_seq, cur_seq)
        #         else:
        #             cur_seq = 1
        # return max_seq
        
        # opt: Hash set + intelligence seq building
        # place all nums in hash set to allow O(1) look up
        # for each num, if n-1 not in set, use while loop buliding up seq by checking if x+1 in the set, if yes, cur+=1, x+=1. update the max_seq

        max_seq = 0
        numSet = set(nums)

        for n in numSet:
            if n - 1 not in numSet:
                x = n
                cur_seq = 1

                while x + 1 in numSet:
                    cur_seq +=1
                    x += 1
                max_seq = max(max_seq, cur_seq)
        return max_seq


