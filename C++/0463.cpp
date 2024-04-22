#include <vector>

class Solution {
public:
    int dfs(int posx, int posy, std::vector<std::vector<int>>& grid, int rows, int cols){

        if (posx == rows || posx == -1 || posy == cols || posy == -1 || grid[posx][posy] == 0) {
            return 1;
        } 

        if(grid[posx][posy] == -1){
            return 0;
        }
        grid[posx][posy] = -1;

        return (
        dfs(posx+1, posy, grid, rows, cols) + 
        dfs(posx-1, posy, grid, rows, cols) + 
        dfs(posx, posy+1, grid, rows, cols) + 
        dfs(posx, posy-1, grid, rows, cols)
        );
    }
    int islandPerimeter(std::vector<std::vector<int>>& grid) {
        int ans = 0;
        int rows = grid.size();
        int cols = grid[0].size();
        
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                if(grid[i][j] == 1){
                    ans += dfs(i, j, grid, rows, cols);
                }
            }
        }
        return ans;
    }
};

// Topic: DFS
// Time Complexity: O(n)
// Space Complexity: O(n)