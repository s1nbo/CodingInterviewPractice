#include <vector>
#include <algorithm>

class Solution {
public:
    int bagOfTokensScore(std::vector<int>& tokens, int power) {
        std::sort(tokens.begin(), tokens.end());
        int score = 0, max_score = 0, left = 0, right = tokens.size()-1;

        while(left <= right){
            if (power >= tokens[left]){
                power -= tokens[left];
                score++;
                left++;
                max_score = std::max(max_score, score);
            } else if(score > 0){
                power += tokens[right];
                score--;
                right--;
            } else break;
        }
        return max_score; 
    }
};
// Topic: greedy, two pointers
// Time Complexity: O(nlogn)
// Space Complexity: O(1)
