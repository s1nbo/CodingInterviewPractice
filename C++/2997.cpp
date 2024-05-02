#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k){
        int xor_val = 0, ans = 0;

        for(int i: nums) xor_val ^= i;
        
        while(k || xor_val){
            ans += ((k%2) != (xor_val%2));
            k /= 2;
            xor_val /= 2;
        }
        return ans;
    }
};

// Topic: Bit Manipulation
// Time Complexity: O(n)
// Space Complexity: O(1)