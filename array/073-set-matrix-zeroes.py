class Solution:
    def setZeroes(self, matrix):
        # Your code goes here
        # [1, 1, 1]
        # [1, 0, 1]
        # [1, 1, 1]
        # traverse the matrix, if matrx[m][n] == 0, list_m_zero[m] = 1, list_n_zero[n] = 1
        # traverse the matrix again, if ist_m_zero[m] or list_n_zero[n], set the cell to zero
        # time O(m*n), space O(m + n)

        # opt: use first row and first col to store if that row or col should be zeroed
            # first_row_zero
            # first_col_zero
        # time O(m*n), space O(1)

        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # check first row
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # check first col 
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
                
        # Use first row/column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # fill zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] ==0:
                    matrix[i][j] = 0
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0




