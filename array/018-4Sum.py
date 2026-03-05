class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # naive: check all quadruplets. time O(n^4)
        # better: sort the array, easy to deduplicate
            # for each number, apply 3 sum 
                # 3 sum: interate through each number, for the rest arr apply two pointers
            # time: O(n^3), auxilary space: O(1), output sapce: O(num of quadruplets)
        
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                # two pointers
                l, r = j+1, n-1
                while l < r:
                    cur_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if cur_sum > target:
                        r -= 1
                    elif cur_sum < target:
                        l += 1
                    else: #cur_sum == target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        r -= 1
                        l += 1
                        while l < r and nums[l] == nums[l -1]:
                            l +=1
                        while l < r and nums[r] == nums[r +1]:
                            r -=1
        return res
