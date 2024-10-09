#include <string>

class Solution {
public:
    int minAddToMakeValid(std::string s) {
        int ans = 0;
        int o = 0;
        for (auto c : s){
            if(c == '('){
                o += 1;
            } else if(o == 0) {
                ans += 1;
            } else {
                o -= 1;
            }
        }
        return ans + o;
    }
};

// Topic: String
// Time Complexity: O(n)
// Space Complexity: O(1)