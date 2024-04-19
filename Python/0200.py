from typing import List

class Solution:
    def dfs(self, posx, posy):        
        if posx == self.rows or posy == self.cols or posx == -1 or \
        posy == -1 or self.grid[posx][posy] == "0": return
        
        self.grid[posx][posy] = "0"

        self.dfs(posx+1, posy)
        self.dfs(posx-1, posy)
        self.dfs(posx, posy+1)
        self.dfs(posx, posy-1)

        return

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        ans = 0
        self.rows = len(grid)
        self.cols = len(grid[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == "1":
                    ans += 1
                    self.dfs(i, j)

        return ans 

# Topic: Dfs
# Time Complexity: O(n*m)
# Space Complexity: O(1)