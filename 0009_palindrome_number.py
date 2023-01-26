class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x)//2):
            if x[i] == x[-i-1]: # cause python is 0 indexed
                pass
            else:
                return False
        return True


"""
Input: integer
Output: boolean

We convert the integer to a string and check if it is a palindrome.

Time Complexity: O(n)
Space Complexity: O(n)
"""

        