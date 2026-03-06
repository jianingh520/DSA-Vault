class Solution:
    def getFloorAndCeil(self, nums, x):
        # floor of x: the largest elemnt that <= x
            # init l, r search range, if nums[m] <= x, update res=m, search right
            # otherwise, search left
        # ceiling of x: the smallest element that >= x -> lower bound
            # init l, r search range, if nums[m] >= x, update res= m, search left
            # otherwise, search right
        # time O(logn), space O(1)
        floor = self.getFloor(nums, x)
        ceil = self.getCeil(nums, x)
        floor_val = nums[floor] if floor != -1 else -1
        ceil_val = nums[ceil] if ceil != -1 else -1
        return floor_val, ceil_val

    def getFloor(self, nums, x):
        l, r = 0, len(nums)-1
        res = -1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] <= x: # potential floor
                res = m
                l = m + 1 # search right
            else:
                r = m -1 # search left
        return res
        
    def getCeil(self, nums, x):
        l, r = 0, len(nums)-1
        res = -1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] >= x: # potential ceil
                res = m
                r = m - 1 # search left
            else:
                l = m + 1 # search right
        return res