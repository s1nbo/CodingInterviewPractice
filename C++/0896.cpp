#include <vector>

class Solution {
public:
    bool isMonotonic(std::vector<int>& nums) {
        if (nums.size() == 1) return true;
        
        bool increase = 0, decrease = 0;
        int current = nums[0];

        for(int i = 1; i < nums.size(); i++){
            if (nums[i] < current) increase = 1;
            if (nums[i] > current) decrease = 1;
            if (increase && decrease) return false;
            current = nums[i];
        }
        return true;
    }
};
// Time Complexity: O(n)
// Space Complexity: O(1)