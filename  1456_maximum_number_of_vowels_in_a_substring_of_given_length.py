class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e","i","o","u"}
        left = 0
        answer = 0
        current = 0

        for right in range(len(s)):
            current += 1 if s[right] in vowels else 0 # add vowels
            
            if right - left + 1 > k: # check if window is greater than k
                current -= 1 if s[left] in vowels else 0 # remove vowels
                left += 1
            
            answer = max(current, answer) # update answer

        return answer


"""
Input: String, Integer
Output: Integer

We create a set of vowels, a left pointer, an answer variable, and a current variable.

We iterate through the string.
We add 1 to the current variable if the current letter is a vowel.

We check if the window is greater than k.
If it is, we remove 1 from the current variable if the left letter is a vowel.
We increment the left pointer.

We update the answer variable with the max of the current variable and the answer variable.

Finally, we return the answer variable.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1)
"""
