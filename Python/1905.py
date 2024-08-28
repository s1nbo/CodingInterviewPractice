from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ans = 0
        rows, cols = len(grid1), len(grid1[0])
        def island(x, y):
            if x < 0 or y < 0 or x >= rows or y >= cols or grid2[x][y] == 0:
                return True
            
            grid2[x][y] = 0

            left = island(x, y-1)
            right = island(x, y+1)
            up = island(x-1, y)
            down = island(x+1, y)
            return left and right and up and down and grid1[x][y]
        

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j]:
                    ans += island(i, j)
                    
        return ans
    
# Topic: Depth First Search
# Time Complexity: O(n*m)
# Space Complexity: O(n*m)
        