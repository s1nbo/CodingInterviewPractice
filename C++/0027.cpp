#include <vector>

class Solution {
public:
    int removeElement(std::vector<int>& nums, int val) {
        int idx = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[idx++] = nums[i];
            }
        }
        return idx;
    }
};

// Topic: Array
// Time Complexity: O(n)
// Space Complexity: O(1)