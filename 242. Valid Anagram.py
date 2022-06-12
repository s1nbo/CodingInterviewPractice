class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters_in_s = {} # maps letters (char) -> how often they appeared s
        letters_in_t = {} # maps letters (char) -> how often they appeared t

        # iterate through s and t and add the letters to the dictionaries
        for i in s:
            if i in letters_in_s:
                letters_in_s[i] += 1
            else:
                 letters_in_s[i] = 1

        for i in t:
            if i in letters_in_t:
                letters_in_t[i] += 1
            else:
                 letters_in_t[i] = 1
        
        # check if the dictionaries are equal
        for i in letters_in_s:
            if i in letters_in_t: # important, because if i is not in letters_in_t, it will be a key error
                if letters_in_s[i] != letters_in_t[i]:
                    return False
            else:
                return False
        
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