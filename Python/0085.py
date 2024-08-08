from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        direction = [[0,1], [1,0], [0, -1], [-1,0]]

        ans = []
        r, c = rStart, cStart
        steps = 1 # Stepsize
        i = 0 # Direction
        while(len(ans) < rows*cols):
            for _ in range(2):
                dr, dc = direction[i]
                for _ in range(steps):
                    if (0 <= r < rows) and (0 <= c < cols):
                        ans.append([r, c])
                    r, c = + r + dr, c + dc
                i = (i+1)%4
            steps += 1
        
        return ans

# Topic: Array, Math
# Time Complexity: O(rows*cols)
# Space Complexity: O(rows*cols)
