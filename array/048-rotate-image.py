class Solution:
    def rotateMatrix(self, matrix):
        # rotate four corner
        # use 2 pointer (left, right) controlling n, 2 pointer(top, bottom) for controlling m, 
        # top_left to store top left element
        # time: O(m*n), space O(1)
        # n = len(matrix)
        # l, r = 0, n-1
        # while l < r:
        #     for i in range(r-l): # current layer, each position, 
        #         top, bottom = l, r

        #         top_left = matrix[top][l+i]

        #         # move bottom left to top left
        #         matrix[top][l + i] = matrix[bottom-i][l]
                
        #         # move bottom right to bottom left
        #         matrix[bottom-i][l] = matrix[bottom][r-i]

        #         # move top right to bottom right
        #         matrix[bottom][r-i] = matrix[top+i][r]
        #         # move top left to top right
        #         matrix[top+i][r] = top_left

        #     # move to inner layer
        #     l += 1 
        #     r -= 1



        # opt: use matrix operations, transpose the matrix then reverse each row
        # time: O(m*n), space O(1)
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n): # row 0, 1, 2
            for j in range(i + 1, n): # col 1, 2; col 2, 2; col 
                # Swap element at (i, j) with (j, i)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            # Reverse the current row to simulate clockwise rotation
            matrix[i].reverse()


