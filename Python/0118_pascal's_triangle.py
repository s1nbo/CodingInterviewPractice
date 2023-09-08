class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(ans[i-1][j]+ans[i-1][j-1])
            row.append(1)
            ans.append(row)
        return ans


"""
Input: Integer
Output: List of lists of integers

First we need to create a list of lists of integers
We know that the first row is always 1

We can use a for loop to iterate through the rows
Each row will have a 1 at the beginning
Then we fill in the rest of the row with the sum of the previous row's elements
Each row will have a 1 at the end
We append each row to the list of lists

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""