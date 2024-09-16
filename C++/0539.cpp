#include <algorithm>
#include <vector>
#include <string>
#include <sstream>

class Solution {
public:
    int findMinDifference(std::vector<std::string>& timePoints) {
        std::vector<int> minutes;
        for (auto tp : timePoints){
            int h, m;
            char temp;
            std::istringstream(tp) >> h >> temp >> m;
            minutes.push_back(60*h + m);
        }

        std::sort(minutes.begin(), minutes.end());
        int ans = 60*24;

        for(int i = 0; i < minutes.size()-1; ++i){
            ans = std::min(ans, minutes[i+1]-minutes[i]);
        }

        ans = std::min(ans, 60*24-minutes.back()+minutes.front());

        return ans;   
    }
};

// Topic: Array, Sorting, String
// Time Complexity: O(n log n)
// Space Complexity: O(n)