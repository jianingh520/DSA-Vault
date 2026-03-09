class Solution:
    def floorSqrt(self, n: int) -> int:
        # naive: linear search on the range [1, N]. time: O(N), space O(1)
        # optimized: binary search. time O(logN), space O(1)
            # Possible anwser space is sorted (1, 2,3,..N). if certain number squared is less than and equal to n, 
            # then all the smaller number will work. 
            # so we can use binary search to find the largest number whoes squared is less than or equal to n.
                # edge case: n=0

        l, r = 1, n
        res = 0
        while l <= r:
            m = l + (r-l) //2
            if m * m <= n:
                res = m
                # search right
                l = m+1
            else:
                # search left
                r = m-1
        return res
            