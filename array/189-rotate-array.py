class Solution:
    def rotateArray(self, nums, k: int) -> None:
        # naive: store the first k element in the temp
        #.       shift remainding elements
        #        copy the stored temp to the end 
        # time O(n), space O(k)

        # opt: reverse trick
        # reverse the first k, reverse the remaining n-k element, reverse the whole array
        # time O(n), space O(1)
        n = len(nums)
        if n <= 1 or k==0:
            return nums
        k %= n
        # if left rotate
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        self.reverse(nums, 0, n-1)
        return nums
        
        # #if right rotate      
        # # reverse whole
        # self.reverse(nums, 0, n-1)
        # # reverse first k
        # self.reverse(nums, 0, k-1)
        # # reverse remaining
        # self.reverse(nums, k, n-1)

    def reverse(self, nums, l, r):

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -=1