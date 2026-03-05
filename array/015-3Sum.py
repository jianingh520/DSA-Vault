class Solution:
    def threeSum(self, nums):
        # naive: check every triplets: time O(n^3)
        # better: for every i, reduced to two Sum problem for the rest arr (i+1 : n-1): time O(n^2) space O(n) 
            # two sum: use hash map to store element we seen so far, and check if j + k = -i
            # hard to dedup
        # opt: sort nums first, solve 2 sum with 2 pointers.
            # for every i, apply 2 pointer method for the rest of arr
            # if curr_sum too big, r-= 1
            # else: l +=1
            # time: O(n^2), space O(1) for auxilary space
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]]) 
                    # we can move both side or one side
                    l +=1
                    r -=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif total > 0:
                    r -= 1
                else: 
                    l += 1
        return res


