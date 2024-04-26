from typing import List

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = {}

        def dfs(i, remain):
            if remain <= 0:
                return 0
            if i == len(cost):
                return float("inf")
            if (i, remain) in dp:
                return dp[(i, remain)] 
        
            paint = cost[i] + dfs(i+1, remain - 1 - time[i])
            skip = dfs(i+1, remain)
            dp[(i, remain)] = min(skip, paint)
            return dp[(i, remain)]

        return int(dfs(0, len(cost))) # Not safe to return float("inf") as the answer

# Topic: Dynamic Programming
# Time complexity: O(n * k)
# Space complexity: O(n * k) 
