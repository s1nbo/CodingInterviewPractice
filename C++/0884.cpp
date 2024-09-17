#include <string>
#include <unordered_map>
#include <vector>
#include <sstream>

class Solution {
public:
    std::vector<std::string> uncommonFromSentences(std::string s1, std::string s2) {
        std::unordered_map<std::string, int> word_count;
        std::istringstream stream1(s1);
        std::istringstream stream2(s2);
        std::string word;
        std::vector<std::string> ans;

        while (stream1 >> word) {
            word_count[word]++;
        }
        while (stream2 >> word) {
            word_count[word]++;
        }

        for (auto pair : word_count) {
            if (pair.second == 1) {
                ans.push_back(pair.first);
            }
        }
        return ans;
    }
};