from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        dp = {}
        
        def dfs(alice, i, M):
            if i == len(piles):
                return 0
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]
            
            ans = 0 if alice else float('inf')
            temp = 0
            
            for X in range(1, 2*M+1):
                if i + X > len(piles):
                    break
                temp += piles[i+X-1]

                rec = dfs(not alice, i+X, max(M, X))
                ans = max(ans, temp + rec) if alice else min(ans, rec)
            
            dp[(alice, i, M)] = ans
            return ans
        
        return dfs(True, 0, 1)

# Topic: Dynamic Programming, Depth-First Search
# Time Complexity: O(n^3)
# Space Complexity: O(n^2)
        