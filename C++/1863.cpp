#include <vector>

class Solution {
public:
    int dfs(int i, int ans, std::vector<int>& nums){
        if (i == nums.size()) return ans;
        return dfs(i+1, ans^nums[i], nums) + dfs(i+1, ans, nums);
    }
    int subsetXORSum(std::vector<int>& nums) {
        return dfs(0, 0, nums);        
    }
};

// Topic: Bit Manipulation, DFS
// Time Complexity: O(2^n)
// Space Complexity: O(n)