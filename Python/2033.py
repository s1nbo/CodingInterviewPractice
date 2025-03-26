from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        # flatten and sort list
        values = sorted([grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))])
        n = len(values)

        # check if possible
        for i in range(1, n):
            if (values[i] - values[i-1]) % x != 0:
                return -1
        
        # find median, has to be in the list, so can't use regular man formular
        median = values[n//2]
        
        # calculate difference between median and values in steps of x
        ans = 0
        for v in values:
            ans += abs(median-v) // x
        
        return ans

# Time Complexity: O(nlogn)
# Space Complexity: O(n)