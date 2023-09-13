class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        char_amount = {}
        for i in range(len(s1)):
            char_amount[s1[i]] = char_amount.get(s1[i], 0) + 1
        
        
        for i in range(len(s2)):
            if s2[i] in char_amount:
                char_amount_copy = char_amount.copy()
                
                for j in range(i, len(s1)+i):
                    if j >= len(s2):
                        return False
                    elif s2[j] in char_amount_copy:
                        char_amount_copy[s2[j]] -= 1
                    else:
                        break
                
                if all(value == 0 for value in char_amount_copy.values()):
                    return True

        return False


"""
Input: Two strings
Output: Boolean

First we check if the length of s2 is less than s1. If it is, then we know that s1 cannot be a permutation of s2, so we return False.

Next, we create a dictionary that will hold the amount of each character in s1. 
We do this by iterating through s1 and adding each character to the dictionary with a value of 1 if it is not already in the dictionary. 
If it is already in the dictionary, we increment the value by 1.


Next, we iterate through s2. If the current character in s2 is in the dictionary, we create a copy of the dictionary and iterate through s2 again.
We iterate through s2 again starting at the current index and ending at the length of s1 plus the current index.
We do this because we want to check if the characters in s1 are in s2.
If the current character in s2 is in the copy of the dictionary, we decrement the value of the character in the copy of the dictionary by 1.
If the current character in s2 is not in the copy of the dictionary, we break out of the loop.
After we finish iterating through s2, we check if all the values in the copy of the dictionary are 0.
If they are, we return True.
If they are not, we continue iterating through s2.

If we finish iterating through s2 and we never return True, we return False.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""
