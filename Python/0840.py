from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def helper(r, c):
            nums = []
            for i in range(r, r+3):
                for j in range(c, c+3):
                    # Check 1-9
                    if grid[i][j] in nums or not(1 <= grid[i][j] <= 9):
                        return 0
                    else:
                        nums.append(grid[i][j])

            # Vertical
            if not(nums[0]+nums[1]+nums[2] == nums[3]+nums[4]+nums[5] == nums[6]+nums[7]+nums[8] == 15):
                return 0

            # Horizontal
            if not(nums[0]+nums[3]+nums[6] == nums[1]+nums[4]+nums[7] == nums[2]+nums[5]+nums[8] == 15):
                return 0

            # Diagonal
            if not(nums[0]+nums[4]+nums[8] == nums[2]+nums[4]+nums[6] == 15):
                return 0

            return 1

        ROWS, COLS = len(grid), len(grid[0])
        ans = 0

        for r in range(ROWS-2):
            for c in range(COLS-2):
                ans += helper(r, c)

        return ans
    
# Topic: Array, Bruteforce
# Time Complexity: O(rows*cols)
# Space Complexity: O(1)