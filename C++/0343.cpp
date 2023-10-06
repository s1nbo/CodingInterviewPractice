#include <cmath>

class Solution {
public:
    int integerBreak(int n) {
        if(n < 4) return n-1;
        int exp = n / 3;
        switch(n%3) {
            case 0: return pow(3, exp);
            case 1: return pow(3, (exp-1)) * 4;
            case 2: return pow(3, exp) * 2;
        }
        return 1;
    }
};

int main(){
    Solution sol;
    int n = 10;
    int ans = sol.integerBreak(n);
    return 0;
}

// Time Complexity: O(log(n))
// Space Complexity: O(1)