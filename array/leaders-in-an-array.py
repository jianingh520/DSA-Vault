class Solution:
    def leaders(self, nums):
        # maintain a max_ while raverse the arr from the back, 
        # if current value > max_, add to res and update the max
        # reverse res
        # time O(n), space O(1)

        res = []
        if not nums:
            return res
        
        max_value = nums[-1]
        res.append(nums[-1])
        for i in range(len(nums) -2, -1, -1)：
            if nums[i] > max_value:
                res.append(nums[i])
                max_value = nums[i] 
        res.reverse() # time O(n), space O(1) in place; nums[::-1] create copy make space O(n)
        return res
        