
"""
given a non-empty grid ‘mat’ with 'n' rows and 'm' columns consisting of only 0s and 1s. 
All the rows are sorted in ascending order. 
Your task is to find the index of the row with the maximum number of ones. Note: If two rows have the same number of ones, consider the one with a smaller index. 
If there's no row with at least 1 zero, return -1

"""

class Solution:
    """
    naive: traverse the matrix using nested loops and for every row, count
            the number of 1, if we found the max current count, update the index
            Time O(N*M), Space O(1)
    better: since we know all rows are sorted in ASC order, we can speed up how we count
            the 1s in each row by applying binary search. instead of traverse every element in a row, 
            we fine the position of the first 1 using binary search, and subtract that index from the number of columns 
                to get number of 1s are present. 
            Time:  O(n log m), space O(1)
    """
    def row_with_max_1s_naive(self, matrix, n, m):
            cnt_max = 0  # naximum number of 1s found so far
            index = -1   # row index with maximum 1s

            # traverse each row
            for i in range(n):
                cnt_ones = 0  # count of 1s in the current row
                for j in range(m):
                    cnt_ones += matrix[i][j]
                if cnt_ones > cnt_max:
                    cnt_max = cnt_ones
                    index = i

            return index  # return row index with most 1s

    def lower_bound(self, arr, n, x):
        # first index i where arr[i] >= x
        l, r = 0, n-1
        res = n
        while l <= r:
            m = l + (r-l)//2
            if arr[m] >= x:
                res = m
                r = m - 1 # search left to check if smaller index exist
            else:
                l = m + 1 # search right
        return res
    def row_with_max_ls_optimized(self, matrix, n, m):
        index = -1
        cnt_max = 0
        # traverse each row
        for i in range(n):
            # count num of one's
            cnt_ones = m - self.lower_bound(matrix[i], m, 1)
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i
        return index
