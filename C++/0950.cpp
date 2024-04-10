#include <vector>
#include <algorithm>
#include <queue>

class Solution {
public:
    std::vector<int> deckRevealedIncreasing(std::vector<int>& deck) {
        std::sort(deck.begin(), deck.end());
        std::vector<int> ans(deck.size());
        std::queue<int> idx;
        
        for(int i = 0; i < deck.size(); i++){
            idx.push(i);
        }
        for(int card : deck){
            ans[idx.front()] = card;
            idx.pop();
            if(!idx.empty()){
                idx.push(idx.front());
                idx.pop();
            }
        }
        return ans;
    }
};

// Topic: Array
// Time Complexity: O(nlogn)
// Space Complexity: O(n)