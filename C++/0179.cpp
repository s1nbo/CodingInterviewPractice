#include <vector>
#include <string>
#include <algorithm>


class Solution {
public:
    std::string largestNumber(std::vector<int>& nums) {
        std::vector<std::string> ans;
        for(int num : nums){
            ans.push_back(std::to_string(num));
        }

        sort(ans.begin(), ans.end(), []( auto a, auto b) {
            return (b + a) < (a + b);
        });

        if(ans[0] == "0") return "0";
        
        std::string result;
        for (auto str : ans) {
            result += str;
        }
        return result;
        
    }
};

// Topic: Greedy, Sorting
// Time Complexity: O(n log n)
// Space Complexity: O(n)