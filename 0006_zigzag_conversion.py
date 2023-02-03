class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        ans = ""
        next_straight = 2*(numRows-1)

        for i in range(numRows):
            
            for j in range(i, len(s), next_straight):
                ans += s[j]
                
                next_zigzag = j + next_straight - 2 * i
                
                if(i != 0 and i != numRows-1 and next_zigzag < len(s)):
                    ans += s[next_zigzag]
        
        return ans


"""
Input: string and integer
Output: string

First we need to check if the number of rows is 1, if it is then we just return the string.
Next we need to create a variable that will hold the index of the next letter in a straight line.
Then we need to loop through the number of rows.
Then we need to loop through the string starting at the current row and incrementing by the next straight line variable.
Then we need to add the current letter to the answer string.
Then we need to create a variable that will hold the index of the next letter in a zig zag line.
Then we need to check if the current row is not the first or last row and if the next zig zag line index is still in the string.
If it is then we need to add the next letter to the answer string.
Then we need to return the answer string.

Time complexity: O(n) (even though there are two loops, we visit every letter in the string once)
Space complexity: O(n) 
"""