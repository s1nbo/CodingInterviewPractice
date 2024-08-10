from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        ans = 0
        length = len(grid)
        n = len(grid)*3
        matrix = [[0]*n for _ in range(n)]

        for r in range(length):
            for c in range(length):
                r2, c2 = r*3, c*3
                if grid[r][c] == '/':
                    matrix[r2][c2+2] = 1
                    matrix[r2+1][c2+1] = 1
                    matrix[r2+2][c2] = 1

                elif grid[r][c] == '\\':
                    matrix[r2][c2] = 1
                    matrix[r2+1][c2+1] = 1
                    matrix[r2+2][c2+2] = 1
       
        
        def dfs(r, c):
            if(r < 0 or c < 0 or r == n or c == n or matrix[r][c] != 0):
                return
            matrix[r][c] = 1
            neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
            for nr, nc in neighbors:
                dfs(nr, nc)

    
        for r in range(n):
            for c in range(n):
                if matrix[r][c] == 0:
                    dfs(r, c)
                    ans += 1

        return ans

# Topic: DFS
# Time complexity: O(n^2)
# Space complexity: O(n^2)

# Idea: Change resoulution of the grid to 3 times the original size and run DFS to find the number of regions.