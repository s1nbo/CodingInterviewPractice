#include <vector>
#include <string>

class Solution {
public:
    bool dfs(int i, int j, int idx, std::vector<std::vector<char>>& board, std::string word ){
        if(word.length() == idx) return true;
        if(i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != word[idx]) return false;
        char temp = board[i][j];
        board[i][j] = ' ';

        bool ans = dfs(i+1, j, idx+1, board, word) || dfs(i-1, j, idx+1, board, word) || dfs(i, j+1, idx+1, board, word) || dfs(i, j-1, idx+1, board, word);
        
        board[i][j] = temp;
        return ans;
    }

    bool exist(std::vector<std::vector<char>>& board, std::string word) {
        for (int i = 0; i < board.size(); i++){
            for (int j = 0; j < board[0].size(); j++){
                if(dfs(i, j, 0, board, word)){
                    return true;
                }
            }
        }
        return false;
    }
};

// Topic: Array, Backtracking
// Time Complexity: O(N*M*4^L)
// Space Complexity: O(L)