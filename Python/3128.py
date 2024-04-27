from typing import List
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        # Count 1 in each row
        rows_ones = []
        for row in grid:
            rows_ones.append(row.count(1))
        # Count 1 in each column
        cols_ones = []
        for col in range(len(grid[0])):
            count = 0
            for row in range(len(grid)):
                if grid[row][col] == 1:
                    count += 1
            cols_ones.append(count)

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    vertical = rows_ones[row] - 1
                    horizontal = cols_ones[col] - 1
                    ans += vertical * horizontal
                            
 
        return ans
        
# Topic: Array
# Time Complexity: O(n^2)
# Space Complexity: O(n)
      