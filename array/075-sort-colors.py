class Solution:
    def sortZeroOneTwo(self, nums):
        # 3 counters to count 0, 1, 2. overwrite array with that many 0, 1, 2
            # time O(n), space O(1)
        
        # Dutch National Flag algorithm.
        l, m, h = 0, 0, len(nums) -1

        while m < h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                m += 1
                l += 1
            elif nums[m] == 1:
                m +=1
            else:
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
        