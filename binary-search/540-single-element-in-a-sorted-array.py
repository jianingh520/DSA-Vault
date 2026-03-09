class Solution:
    def singleNonDuplicate(self, nums):
        # naive: XOR or linear search. Time O(N), Space O(1)
            # linear search to check every element in the array until we find the single element.
            # xor. use 2 properties of xor: a^a =0 and a^0=a. xor all elem in the arr, all the duplicate will result in 0 and we will be left with the single number
        # better: binary search. Time O(logN), Space O(1)  
            # since the array is sorted, and all element except one appear exactly once. before we encounter unique element, each pair starts at a even index and ends at a odd index. But once we meet the unique element, this pairing pattern breaks and the shift happens after that unique element. Thus, we can use this pattern to cut the search space in half using binary search.
                # if the paring pattern holds, search right
                # if the paring pattern breaks, search left
                # edge case:
                    # n == 1 
                    # nums[0] != nums[1], 
                    # nums[n-1] != nums[n-2],
                    # set search range [1, n-2]
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]

        l, r = 1, n-2
        while l <= r:
            m = l + (r-l)//2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]

            # paring pattern holds
            if (m%2 == 0 and nums[m] == nums[m+1]) or \
                (m%2==1 and nums[m] == nums[m-1]) : # even: start. odd index: end index
                # search right
                l = m + 1

            # paring pattern breaks        
            else:
                # search left
                r = m - 1
        return -1

