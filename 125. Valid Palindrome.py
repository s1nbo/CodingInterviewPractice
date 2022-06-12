class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)) # '' joined with every char in s that is accepted by the filter
        # the filter only accepts alpha numeric chars (letters and numbers)
        s = s.lower() # changes all letters to lowercase
        
        left, right = 0, len(s)-1
        
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True


"""
Input: string
Output: boolean

Start by rebuilding the string without any non-alphanumeric characters.
'' empty string joined with every char in s that is accepted by the filter
the filter only accepts alpha numeric chars (letters and numbers)

left and right are the indices of the left and right ends of the string.

increment left and decrement right until they meet each other.
if the chars at left and right are not equal, return False.

Time Complexity: O(n)
Space Complexity: O(1)
"""