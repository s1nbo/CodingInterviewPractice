class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        length = len(cost)+1
        dp = [0] * length

        for i in range(2, length):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[length-1]

# Time Complexity: O(n)
# Space Complexity: O(n)