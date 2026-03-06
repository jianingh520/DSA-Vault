class Solution:
    def countOccurrences(self, nums, target):
        # Your code goes here
        # naive: linear search. time O(n)
        # better: binary search for first and last index of target. res = last-first+1
            # starting position: the first index that = target
                # init l, r search range, if nums[m] == target, update res = m, search left
                # if nums[m] < target, search right 
                # if nums[m] > target, search left 
            # ending postion: the last index that = target
                # init l, r search range, if nums[m] == target, update res = m, search right
                # if nums[m] < target, search right 
                # if nums[m] > target, search left 
            # time O(logn), space O(1)

        first = self.searchFirst(nums,target)
        last = self.searchLast(nums, target)
        if first == -1:
            return 0
        return last - first + 1

    def searchFirst(self, nums, target):
        l, r = 0, len(nums)-1
        res = -1
        while l <= r:
            m = l +(r-l)//2
            if nums[m] == target:
                res = m
                r = m -1 # search left
            elif nums[m] < target:
                l = m +1 # search right
            else: # nums[m] > target
                r = m - 1# search left
        return res

    def searchLast(self, nums, target):
        l, r = 0, len(nums)-1
        res = -1
        while l <= r:
            m = l +(r-l)//2
            if nums[m] == target:
                res = m
                l = m +1 # search right
            elif nums[m] < target:
                l = m +1 # search right
            else: # nums[m] > target
                r = m - 1# search left
        return res        