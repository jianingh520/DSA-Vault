class Solution:
    def maxLen(self, arr):
        # Your code goes here
        # naive: check every subarray and its sum, if sum=0, update the best_len. time O(n^3) 
        # better: use prefix sum, check every pair of sum using prefix[j] - prefix[i]. time O(n^2). i, i+1-n
        # optimized: use hashmap to store {prefix: first index}, every step we check if diff(current sum) in prefix, if yes, get first index and update the best_len. otherwise, if cur_sum not in map, add to map
            # time O(n), space O(n)


        prefix = {0: -1} #{prefix sum: first idx}
        best_len = 0 
        cur_sum = 0
        for i, need in enumerate(arr):
            cur_sum += x
            need = cur_sum
            if need in prefix:
                best_len = max(best_len, i - prefix[need])
            if cur_sum not in prefix:
                prefix[cur_sum] = i
        return best_len