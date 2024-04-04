#include <string>
#include <algorithm>

class Solution {
public:
    int maxDepth(std::string s) {
        int cur = 0, ans = 0;
        for(auto i : s){
            if(i == '(') ans = std::max(ans, ++cur);
            else if(i == ')') --cur;
        }
        return ans;
    }
};

// Topic: String
// Time Complexity: O(n)
// Space Complexity: O(1)