class Solution:
    def subarraySum(self, nums, k):
      # 2 pointer l, r maintain sliding window -> only work with postive number, how about negative number?
      
      # naive: check every subarray and its sum, time O(n^3) -> heaving computation: repeated sum
      # idea: prefix sum, loop over all pair -> time O(n^2) 
      # opt: two sum on prefix arr
        # prefix[current] - prefix[previous] = k
        # time O(n), Space O(n)
        cnt = 0
        prefix_sum = {0: 1} # {prefix_sum, freq} # if ask longest subarry, store first index
        cur_sum = 0
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            if diff in prefix_sum:
                cnt += prefix_sum[diff]
            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)
        return cnt
        
    # [1, 1, 1], k = 2
    # i = 0, cur_sum=1, target = 1-2 = -2,  prefix_sum = {0: 1, 1: 1}
    # i = 1, cur_sum =2, target=2-2=0, cnt =1, prefix_sum = {0: 1, 1: 1, 2:1}
    # i = 2, cur_sum = 3, target=3-2=1, cnt =2. prefix_sum = {0: 1, 1: 1, 2:1, 3:1}
