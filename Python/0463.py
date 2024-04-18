from typing import List

class Solution:
    def dfs(self, posx, posy):
        if posx == self.rows or posx == -1 or posy == self.cols or posy == -1 or self.grid[posx][posy] == 0:
            return 1
        if self.grid[posx][posy] == -1:
            return 0
        self.grid[posx][posy] = -1

        return self.dfs(posx+1, posy) + self.dfs(posx+1, posy) + self.dfs(posx, posy+1) + self.dfs(posx, posy-1)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid

        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 1:
                    ans += self.dfs(i, j)

        return ans

# Topic: DFS
# Time Complexity: O(n)
# Space Complexity: O(1)
        