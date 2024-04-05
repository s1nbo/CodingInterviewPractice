#include <string>

class Solution {
public:
    std::string makeGood(std::string s) {
        std::string stack;
        for(auto c : s) {
            if(!stack.empty() && abs(c - stack.back()) == 32) {
                stack.pop_back();
            } else {
                stack.push_back(c);
            }
        }
        return stack;
    }
};

// Topic: String, Stack
// Time Complexity: O(n)
// Space Complexity: O(n)
