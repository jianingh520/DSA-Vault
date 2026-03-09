class Solution:
    def minimumRateToEatBananas(self, nums, h):
       # naive: linear search on [1, max(nums)]. Time O(M*N) where M = max(nums), Space O(1)
       # optimized: binary search on [1, max(nums)] to find minimum k to finish all bananas within h hours
            #  if certain k (eating rate) works, koko can finish all within h hours, then all higher speeds will also works. This allow us to apply binary search on search space to find the minimum k where Koko can finish the bananas within the given hours.
            # edge case: 
                # one pile 
            # Time O(logM * N). Space O(1)

        l, r = 1, max(nums)
        res = max(nums)
        while l <= r:
            # potential eating rate
            m = l + (r-l)//2
            # time needed with this eating rate
            time = 0
            for n in nums:
                time += math.ceil(n / m)
                if time > h:
                    break
            if time <= h:
                res = m
                # search left, try smaller speed
                r = m -1
            else:
                # search right, try larger speed
                l = m +1
        return res 
            