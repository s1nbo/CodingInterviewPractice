#include <string>
#include <vector>

class Solution {
public:
    std::string minRemoveToMakeValid(std::string s) {
        std::vector<char> ans;
        int counter = 0;
        for (char c : s) {
            counter += (c == '(');
            if (c == ')' && counter > 0){
                ans.push_back(c);
                counter--;
            }
            else if(c != ')') ans.push_back(c);
        }
        std::vector<char> filtered;
        for (auto it = ans.rbegin(); it != ans.rend(); ++it) {
            if (*it == '(' && counter > 0) {
                counter--;
            } else {
                filtered.push_back(*it);
            }
        }
        return std::string(filtered.rbegin(), filtered.rend());
    }
};

// Topic: Stack, String
// Time Complexity: O(n)
// Space Complexity: O(n)