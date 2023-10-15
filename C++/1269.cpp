class Solution {
public:
    const int MOD = 1e9+7;
    int numWays(int steps, int arrLen) {
        std::vector<std::vector<long>> dp(steps + 1, std::vector<long>(std::min(arrLen, steps) + 1, -1));
        return dfs(0, steps, arrLen, dp);
    }
    int dfs(int idx, int steps, int arrLen, std::vector<std::vector<long>>& dp){
        if(steps == idx && idx == 0) return 1;
        if(idx < 0 || idx >= arrLen || idx > steps) return 0;
        if (dp[steps][idx] != -1) return dp[steps][idx];
        
        long tmp = dfs(idx, steps-1, arrLen, dp); // stay
        tmp += dfs(idx-1, steps-1, arrLen, dp); // left
        tmp += dfs(idx+1, steps-1, arrLen, dp); // right

        dp[steps][idx] = tmp % MOD;
        return dp[steps][idx];

    }
};
