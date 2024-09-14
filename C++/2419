#include <vector>

class Solution {
public:
    int longestSubarray(std::vector<int>& nums) {
        int size = 0, ans = 0, maximum = 0;

        for (auto n : nums) {
            if(n > maximum) {
                maximum = n;
                size = 1;
                ans = 1;
            } else if(n < maximum) { 
                ans = std::max(size, ans);
                size = 0;
            } else {
                size++;
            }
        }
        return std::max(size, ans);        
    }
};

// Topic: Array
// Time Complexity: O(n)
// Space Complexity: O(1)