class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        for i in range(len(x_str)//2):
            if x_str[i] == x_str[-i-1]: # cause python is 0 indexed
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

        