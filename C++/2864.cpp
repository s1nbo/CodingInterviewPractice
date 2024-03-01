#include <string>
#include <bitset>

class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        return string(count(s.begin(), s.end(), '1')-1, '1') + string(s.length()-count(s.begin(), s.end(), '1'), '0') + '1';

    }
};

// Time Complexity: O(n)
// Space Complexity: O(1)