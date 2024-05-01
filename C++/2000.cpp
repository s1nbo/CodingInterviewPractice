#include <string>
#include <algorithm>

class Solution {
public:
    std::string reversePrefix(std::string word, char ch) {
        int idx = word.find(ch);
        if(idx != -1) std::reverse(word.begin(), word.begin()+idx+1);
        return word;
             
    }
};

// Topic: String
// Time Complexity: O(n)
// Space Complexity: O(1)

