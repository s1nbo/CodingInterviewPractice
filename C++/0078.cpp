#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> merge(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end());
        int idx = 0;
        while(idx < intervals.size()-1){
            if(intervals[idx][1] >= intervals[idx+1][0]){
                intervals[idx] = {std::min(intervals[idx][0], intervals[idx+1][0]), std::max(intervals[idx][1], intervals[idx+1][1])};
                intervals.erase(intervals.begin() + idx + 1);
            } else {
                ++idx;
            }
        }
        return intervals;
    }
};

// Topic: Array, Sorting
// Time Complexity: O(nlogn)
// Space Complexity: O(1)