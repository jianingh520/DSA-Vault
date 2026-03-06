class Solution:
    def lowerBound(self, nums, x):
        # lower bound of x: first and smallest index where the value >= x 
        # if no such index is found, return the size of the array.
        
        # naive: linear search. time O(n)
        # better: since arr is sorted, we can apply binary search. 
            # initialize l, r search range.
                # if nums[m]>= x, update the res=m, and search left 
                # otherwise, search right
            # time O(logn), space O(1)
        
        l, r = 0, len(nums) -1
        res = len(nums)
        while l <= r:
            m = l + (r-l)//2
            if nums[m] >= x:
                res = m
                r = m -1
            else: #nums[m] < x
                l = m +1
        return res
        # important edge case: nums = [1,2,3], x = 10, res=len(nums)=3


        # method 2: other lower bound vesion
        # maintain search space [l,r), final res = l

        # l, r = 0, len(nums)

        # while l < r:
        #     m = (l + r)//2

        #     if nums[m] >= x:
        #         r = m
        #     else:
        #         l = m + 1

        # return l
       


