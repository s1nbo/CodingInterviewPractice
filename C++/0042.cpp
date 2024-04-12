#include <vector>
#include <algorithm>

class Solution {
public:
    int trap(std::vector<int>& height) {
        int n = height.size();
        std::vector <int> left(n);
        std::vector <int> right(n);
        int ans = 0;
        left[0] = height[0];
        right[n-1] = height[n-1];
        
        for (int i = 1; i < n; i++) left[i] = std::max(left[i-1], height[i]);
        
        for (int i = n - 2; i >= 0; i--) right[i] = std::max(right[i+1], height[i]);

        for (int i = 0; i < n; i++) ans += std::min(left[i], right[i]) - height[i];

        return ans;
    }
};

// Topic: Array
// Time Complexity: O(n)
// Space Complexity: O(n)

