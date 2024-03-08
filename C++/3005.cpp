#include <vector>
#include <unordered_map>

class Solution {
public:
    int maxFrequencyElements(std::vector<int>& nums) {
        std::unordered_map<int, int> nums_count;
        int current_max = 0;
        int ans = 0;

        for (int num : nums) {
            nums_count[num]++;
        }
        for (const auto& value : nums_count) {
            if (value.second > current_max) {
                current_max = value.second;
                ans = value.second;
            }
            else if(value.second == current_max) {
                ans += value.second;
            }
        }
        return ans;
    }
};
// Topic: Hash Table
// Time Complexity: O(n)
// Space Complexity: O(n)