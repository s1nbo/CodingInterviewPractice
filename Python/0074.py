class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        col = list(zip(*matrix))[0]

        l, r = 0, len(col)-1
        while l <= r:
            m = (l+r) // 2
            if col[m] > target:
                r = m - 1
            elif col[m] < target:
                l = m + 1
            else:
                return True

        row = matrix[l-1]

        l, r = 0, len(row)-1
        while l <= r:
            m = (l+r) // 2
            if row[m] > target:
                r = m - 1
            elif row[m] < target:
                l = m + 1
            else:
                return True
        return False
    

"""
Input: matrix of integers, integer
Output: boolean

We flip the matrix using list and zip to get the first column.

We use binary search through the first column to find the correct row.
Then we use binary search through the row to find the target.
If the target is not found, we return False.

Time Complexity: O(log(n*m)) where n is the number of rows and m is the number of columns
Space Complexity: O(1)
"""
    
