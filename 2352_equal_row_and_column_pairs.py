class Solution:
    def equalPairs(self, grid) -> int:
        answer = 0
        rows = {}
        cols = {}
        for i in grid:
            key = "".join(str(i))
            rows[key] = rows.get(key, 0) + 1
        
        """
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid[0])):
                col.append(grid[j][i])
        """
        # zip(*n) flips cols and rows, makes each column a tuple in a list
        for col in zip(*grid): 
            key = "".join(str(list(col)))
            cols[key] = cols.get(key, 0) + 1

        for row in rows:
            if row in cols:
                answer += rows[row] * cols[row]

        return answer


"""
Nice Answer:
pairs = 0
cnt = Counter(tuple(row) for row in grid)
for tpl in zip(*grid):
        pairs += cnt[tpl]
return pairs
"""

"""
Input: 2D List of integers
Output: Integer

We iterate through the rows and columns and store the rows and columns in a dictionary.
We then iterate through the rows and check if the row is in the columns dictionary.
If it is, we add the number of times the row appears in the columns dictionary to the answer.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""