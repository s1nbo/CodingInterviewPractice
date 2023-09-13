class Solution:
    def longestCommonPrefix(self, strs) -> str:

        ans = ""

        for i in range(len(strs[0])):
            for strings in strs:
                
                if i >= len(strings) or strings[i] != strs[0][i]:
                    return ans
                
                ans += strs[0][i]
                    
        return ans
            

"""
Input: List of strings
Output: Longest common prefix

We use the first string as the base string to compare to the rest of the strings.
We iterate through the characters of the first string and compare it to the characters of the rest of the strings.

If the first string is longer than of one of the strings, we return the ans. Or if the characters don't match, we return the ans.
Else we add the character to the ans.

Time Complexity: O(n * m) where n is the length of the first string and m is the number of strings
Space Complexity: O(n) where n is the length of the first string
"""