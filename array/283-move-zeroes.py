class Solution:
    def moveZeroes(self, nums):
        # two pass
        # # slow pointer i to build the array
        # # fast pointer j to scan the array, if j != 0, place to i, and i+=1
        # #                                   if j ==0, zeros+=1
        # # fill all the zero at the end of array
        # # time O(n), space O(1)
        
        # if not nums:
        #     return

        # i = 0
        # for j in range(len(nums)):
        #     if nums[j] != 0:
        #         nums[i] = nums[j]
        #         i += 1

        
        # for k in range(i, len(nums)):
        #     nums[k] = 0


        # optimize: one pass
        # i for the next nonzero
        # j faster pointer to scan input to check non-zero, if it is, swap

        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            