class Solution:
    def pascalTriangleI(self, r, c): 
        # return the value at the rth row and cth column (1-indexed) 
        # element is C(r-1, c-1)
            # time Complexity: O(min(c,r−c)), the loop runs for min(c−1,r−c) iterations because binomial coefficients are symmetric.
            # space Complexity: O(1), constant additional space is used.
        n = r - 1
        k = c - 1

        res = 1

        # compute C(n, k) using iterative formula
        for i in range(k):
            res *= (n - i)
            res //= (i + 1)

        return res

    def pascalTriangle(self,r): 
        # build whole triangle
        # start with the first row containing a single 1 and iteratively build each subsequent row using the property that every element (except the first and last) is the sum of the two elements directly above it from the previous row. 
            # time O(n^2), space O(n^2) storing the entire pascal triangle. auxiliary space O(1)
        triangle = []
        for i in range(r):
            row = [1] * (i+1)

            # Fill elements from index 1 to i-1 (middle values)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1]+triangle[i-1][j]
            triangle.append(row)
        return triangle
