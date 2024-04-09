#include <vector>
#include <algorithm>

class Solution {
public:
    int timeRequiredToBuy(std::vector<int>& tickets, int k) {
        int target = tickets[k], ans = 0, i = 0;
        for(; i <= k; i++) {
            ans += std::min(target, tickets[i]);
        }
        target--;
        for(; i < tickets.size(); i++) {
            ans += std::min(target, tickets[i]);
        }
        return ans;
    }
};

// Topic: Array
// Time Complexity: O(n)
// Space Complexity: O(1)