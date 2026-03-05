class Solution:
    def twoSum(self, nums, target):
        # naive, explore all combination use 2 for loop. 
            # time  O(n^2). space :O(1)
        # traverse arr while maintain hash map store the num, idex we've seen for far. when we check a new element, we look back and see if we found a number that sume to target

        seen = {} # {num: idx}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]
            seen[nums[i]] = i
        return -1