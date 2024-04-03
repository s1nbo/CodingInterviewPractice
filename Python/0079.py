from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = [[False] * len(board[0]) for _ in range(len(board))]

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[idx]:
                return False

            visited[i][j] = True

            if dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1):
                return True
            
            visited[i][j] = False
            
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False 
                    
# Topic: Backtracking, DFS
# Time Complexity: O(N * 4^L) N is the number of cells in the board and L is the length of the word
# Space Complexity: O(N) N is the number of cells in the board