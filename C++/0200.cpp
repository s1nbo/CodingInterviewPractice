#include <vector>

class Solution {
public:
    void dfs(std::vector<std::vector<char>>& grid, int posx, int posy, int rows, int cols){

        if(posx == rows || posy == cols || posx == -1 || posy == -1 || grid[posx][posy] == '0') return;

        grid[posx][posy] = '0';

        dfs(grid, posx+1, posy, rows, cols);
        dfs(grid, posx-1, posy, rows, cols);
        dfs(grid, posx, posy+1, rows, cols);
        dfs(grid, posx, posy-1, rows, cols);

        return;

    }

    int numIslands(std::vector<std::vector<char>>& grid) {
        int ans = 0;
        int rows = grid.size();
        int cols = grid[0].size();

        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                if(grid[i][j] == '1'){
                    ans++;
                    dfs(grid, i, j, rows, cols);
                }
            }
        }
        return ans;
    }
};

// Topic: Dfs
// Time Complexity: O(n*m)
// Space Complexity: O(n*m)