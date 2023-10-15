class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters_s = {} # maps letters (char) -> how often they appeared s
        letters_t = {} # maps letters (char) -> how often they appeared t

        # iterate through s and t and add the letters to the dictionaries
        for i in s:
            letters_s[i] = letters_s.get(i, 0) + 1
        for i in t:
            letters_t[i] = letters_t.get(i, 0) + 1
        
        # check if the dictionaries are equal
        for i in letters_s:
            if i in letters_t and letters_s[i] == letters_t[i]: continue
            else: return False
        
        return True
   
                    
"""
Input: two strings
Output: boolean

Check if the same letters are in both strings.

First check if the length of the strings are the same.
If they are not the same, return False.

Create a dictionary to store the letters in s and t and their frequency.
go through s and t and add the letters to the dictionary.

go through the dictionary and check if the letters in s are also in t.
If they are not, return False.

Time Complexity: O(n)
Space Complexity: O(n)
"""