from typing import List

class MatrixOps:
    """
    Matrix multiplication from scratch.
    A_mat1: (m x k), B_mat2: (k x n) → C_res: (m x n)

    Naive: triple loop
        Each element x[i][j] is the sum of product of elements of i 
        th row of matrix A and j th column of matrix B.

        Time O(m·n·k), Space O(m·n) for output, O(1) for auxiliary space 
    
    follow-up: sparse matrix -- matrix is too big but only a few non-zero elemnt
    Optimized: use some data structure (e.g. array of array) to store non-zero element
        
        Time O(m·k·n) worst case (all non-zero),
             O(nnz_A · avg_nnz_B_row) average case for sparse matrices.
        Space O(m·n) output, O(m⋅k+k⋅n) auxiliary space for store compress matrix


    """
    def multiply_naive(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # mat1 : m x k
        # mat2 : k x n
        # res = mat1 * mat2 : m * n
        # time O(m·k·n) -- triple loop
        # space O(m·n) for output, O(1) for auxiliary space
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])

        res = [[0]* n for _ in range(m)]
        
        for i in range(m):
            for p in range(k):
                if mat1[i][p]:
                    for j in range(n):
                        res[i][j] += mat1[i][p] * mat2[p][j]
        return res


    def _compress_matrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # row0 index -> [(value, col)]
        m, n = len(matrix), len(matrix[0])
        compress_matrix = [[] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    compress_matrix[i].append([matrix[i][j], j])
        return compress_matrix

    def multiply_sparse(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])

        # store non-zero values of each matrix
        A = self._compress_matrix(mat1)
        B = self._compress_matrix(mat2)
        res = [[0] * n for _ in range(m)]

        for i in range(m): # m rows of mat1
            for ele1, p in A[i]: # [val, col], non-zero entries in row i of mat1
                for ele2, j in B[p]: # non-zero entries in row p of mat2
                    res[i][j] += ele1 * ele2 # A[i][p] * B[p]
        return res


# ── TEST CASES ─────────────────────────────────────────────────────────────

def test_matrix():

    # normal: square matrices
    A = [[1, 0], [0, 3]]
    B = [[7, 0], [0, 8]]
    expected = [[7, 0], [0, 24]]
    sol = MatrixOps()
    assert sol.multiply_naive(A, B) == expected
    assert sol.multiply_sparse(A, B) == expected

    # normal: non-square 2x3 times 3x2
    A2 = [[1, 2, 3], [4, 5, 6]]
    B2 = [[7, 8], [9, 10], [11, 12]]
    expected2 = [[58, 64], [139, 154]]
    assert sol.multiply_naive(A2, B2) == expected2
    assert sol.multiply_sparse(A2, B2) == expected2

    # edge: all zeros
    A3 = [[0, 0], [0, 0]]
    B3 = [[1, 2], [3, 4]]
    expected3 = [[0, 0], [0, 0]]
    assert sol.multiply_naive(A3, B3) == expected3
    assert sol.multiply_sparse(A3, B3) == expected3

    # edge: identity matrix
    I = [[1, 0], [0, 1]]
    A4 = [[3, 4], [5, 6]]
    assert sol.multiply_naive(I, A4) == A4
    assert sol.multiply_sparse(I, A4) == A4

    # edge: 1x1 matrices
    assert sol.multiply_naive([[3]], [[4]]) == [[12]]
    assert sol.multiply_sparse([[3]], [[4]]) == [[12]]

    print("all tests passed")


test_matrix()