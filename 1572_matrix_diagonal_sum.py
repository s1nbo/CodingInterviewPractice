class Solution:
    def diagonalSum(self, mat) -> int:
        ans, length = 0, len(mat[0])

        for i in range(length):
            ans += mat[i][i] + mat[i][length-i-1]

        if length % 2 == 1:
            ans -= mat[length//2][length//2]
        
        return ans


"""
Input: square matrix of integers
Output: integer

Initialize a variable to store the sum of the diagonals.
Initialize a variable to store the length of the matrix.

Iterate through the matrix.
    Add the value at the current index of the diagonal to the sum. 
    Add the value at the current index of the reverse diagonal to the sum.

If the length of the matrix is odd, subtract the value at the center of the matrix from the sum.
(Since the center of the matrix is included in both diagonals, it is added twice.)

Return the sum.

Time Complexity: O(n)
Space Complexity: O(1)
"""
