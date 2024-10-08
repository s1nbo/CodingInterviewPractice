#pragma GCC optimize("O3", "unroll-loops")
#include <ios>
#include <iostream>
#include <string>

class Solution {
public:
    int minSwaps(std::string s) {
        std::ios_base::sync_with_stdio(0);
        std::cin.tie(0);
        std::cout.tie(0);
        int ans = 0;
        for(int i=0; i<s.size(); i++){
            ans += (s[i] == '[');
            ans -= (ans > 0 && s[i] == ']');
        }
        return (ans+1) / 2;
    }
};

// Topic: Greedy
// Time Complexity: O(n)
// Space Complexity: O(1)