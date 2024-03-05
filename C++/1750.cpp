#include <string>

class Solution {
public:
    int minimumLength(std::string s) {
        int left = 0, right = s.size()-1;

        while(left < right && s[left] == s[right]){
            char cur = s[left];
            while(left <= right && cur == s[++left]){}
            while(left <= right && cur == s[--right]){}
        }
        return right-left+1;
    }
};

// Topic: Two Pointers
// Time Complexity: O(n)
// Space Complexity: O(1)