#include <string>

class Solution {
public:
    std::string removeKdigits(std::string num, int k) {
        std::string stack = "";
        for (char c : num) {
            while (k && stack.size() && stack.back() > c) {
                stack.pop_back();
                k--;
            }
            if(stack.size() || c != '0') stack.push_back(c);
        }
        
        while(stack.size() && k--)
            stack.pop_back();
        
        return stack.size() == 0 ? "0" : stack;
    }
};

// Topic: Stack
// Time Complexity: O(n)
// Space Complexity: O(n)