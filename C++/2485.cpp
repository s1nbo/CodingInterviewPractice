#include <cmath>

class Solution {
public:
    int pivotInteger(int n) {
        float x = std::sqrt(n*(n+1)/2);
        return (std::floor(x) == x) ? static_cast<int>(x) : -1;
    }
};

// Topic: Math
// Time Complexity: O(1)
// Space Complexity: O(1)