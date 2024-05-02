#include <vector>
#include <unordered_set>

class Solution {
public:
    int findMaxK(std::vector<int>& nums) {
        std::unordered_set<int> nums_set(nums.begin(), nums.end());
        int ans = -1;

        for(int cur : nums_set){
            if (nums_set.find(-cur) != nums_set.end()){
                ans = std::max(ans, cur);
            }
        }
        return ans; 
    }
};

// Topic: Array, Hash Table
// Time Complexity: O(n)
// Space Complexity: O(n)