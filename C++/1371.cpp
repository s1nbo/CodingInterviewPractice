#include <string>
#include <unordered_map>

class Solution {
public:
    int findTheLongestSubstring(std::string s) {
        std::string vowels = "aeiou";
        int ans = 0;
        int mask = 0;
        std::unordered_map<int, int> mask_to_idx;
        mask_to_idx[0] = -1;

        for(int i = 0; i < s.size(); ++i){
            char c = s[i];
            if(vowels.find(c) != std::string::npos){
                mask ^= (c - 'a') + 1;
            }
            if (mask_to_idx.find(mask) != mask_to_idx.end()) {
                ans = std::max(ans, i - mask_to_idx[mask]);
            } else {
                mask_to_idx[mask] = i;
            }
        }
        return ans;
    }
};

// Topic: Array, Bit Manipulation
// Time Complexity: O(n)
// Space Complexity: O(1)