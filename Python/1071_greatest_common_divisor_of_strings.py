class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        max_length = max(len(str1), len(str2))

        for i in range(max_length):
            if str1[i% len(str1)] == str2[i % len(str2)]:
                ans += str1[i% len(str1)]
            else:
                return ""
        
        while len(str1) % len(ans) != 0 or len(str2) % len(ans) != 0:
            ans = ans[:-1]
        
        return ans
    

"""
Input: Two strings
Output: string

First we create our answer string and find the max length of the two strings.

Then we iterate through the max length and check if the characters at the current index of the two strings are equal. 
If they are, we add the character to our answer string. If they are not, we return an empty string.

Then we check if the length of the two strings are divisible by the length of the answer string. 
If they are not, we remove the last character from the answer string and check again.

If the length of the two strings are divisible by the length of the answer string, 
we return the answer string.

Time Complexity: O(n)
Space Complexity: O(n)
"""