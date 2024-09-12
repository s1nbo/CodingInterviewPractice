
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int countConsistentStrings(std::string allowed, std::vector<std::string>& words) {
        std::unordered_set<char> allowedSet(allowed.begin(), allowed.end());
        int ans = 0;

        for (auto word : words){
            bool temp = true;
            for (auto c : word) {
                if (allowedSet.find(c) == allowedSet.end()){
                    temp = false;
                    break;
                }
            }
            ans += temp;
        }
        return ans;
    }
};

// Topic: String
// Time Complexity: O(n * m) where n is the number of words and m is the length of the longest word
// Space Complexity: O(1) as the allowedSet will have at most 26 characters