from functools import cache
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def dfs(xPos, steps):
            if steps == xPos and xPos == 0:
                return 1
            if xPos > steps:
                return 0
            if xPos < 0 or xPos >= arrLen:
                return 0
            
            tmp = 0
            tmp += dfs(xPos-1, steps-1)
            tmp += dfs(xPos, steps-1)
            tmp += dfs(xPos+1, steps-1)
        
            return tmp % MOD

        MOD = 10**9+7
        return dfs(0, steps)

# Time complexity: O(steps*arrLen)
# Space complexity: O(steps*arrLen)