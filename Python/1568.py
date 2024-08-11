class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        def count_island():
            seen = set()
            island = 0

            def dfs(x, y):
                stack = [(x, y)]
                while stack:
                    r, c = stack.pop()
                    for new_r, new_c in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
                        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1 and (new_r, new_c) not in seen:
                            seen.add((new_r, new_c))
                            stack.append((new_r, new_c))
                    

            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1 and (r, c) not in seen:
                        island += 1
                        seen.add((r, c))
                        dfs(r, c)

            return island


        # Already disconnected
        if count_island() != 1:
            return 0
        # Remove one island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_island() != 1:
                        return 1
                    grid[i][j] = 1

        # Rest
        return 2

# Topic: DFS, Graph
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)