class Solution:
    def NthRoot(self, n, m):
        # naive: linear search on [1, M]. Time O(M*N), space O(1)
        # optimized: binary search on [1, M]
            # since the search space is sorted, we can use binary search on to halve search space at every step. 
            # if mid^n == m, return mid
            # if mid^n < m, search right
            # if mid^n > m, search left
            # time: O(log m * n), space: O(1)
        l, r = 1, m
        while l <= r:
            mid = l + (r-l)//2
            # culuate mid ^ N
            ans = 1
            for _ in range(n):
                ans *= mid
                if ans > m:
                    break
            
            if ans == m:
                return mid
            elif ans < m:
               # search right
               l = mid + 1
            else:
                # search left
                r = mid - 1
        return -1
      