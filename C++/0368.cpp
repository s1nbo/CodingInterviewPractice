#include <vector>
#include <algorithm>

class Solution {
    public:
        std::vector<int> largestDivisibleSubset(std::vector<int>& nums) {
            std::sort(nums.begin(), nums.end());
            std::vector<int> dp(nums.size(), 1);
            std::vector<int> prev(nums.size(), -1);
            int maxIndex = 0;
            for (int i = 0; i < nums.size(); ++i) {
                for (int j = 0; j < i; ++j) {
                    if (nums[i] % nums[j] == 0 && dp[i] < dp[j] + 1) {
                        // Update size of the subset and previous index
                        dp[i] = dp[j] + 1;
                        prev[i] = j;
                    }
                }
                // Update maxIndex if we found a larger subset
                if (dp[i] > dp[maxIndex]) {
                    maxIndex = i;
                }
            }
            // Build the result subset by following the prev array
            std::vector<int> result;
            while (maxIndex != -1) {
                result.push_back(nums[maxIndex]);
                maxIndex = prev[maxIndex];
            }
            return result;
        }
    };