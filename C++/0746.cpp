#include <vector>
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int len = cost.size()
        std::vector<int> dp[len+1] = {0};
        for(int i = 2; i <= len; i++){
            dp[i] = std::min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]);
        }
        return dp[len];
    }
};

// Time Complexity: O(n)
// Space Complexity: O(n)