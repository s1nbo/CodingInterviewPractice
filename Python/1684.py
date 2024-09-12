from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = 0

        for word in words:
            temp = True
            for c in word:
                if c not in allowed:
                    temp = False
                    break
            ans += temp

        return ans

# Topic: String
# Time Complexity: O(n*m) where n is the length of words and m is the length of the longest word
# Space Complexity: O(1) as we are using a set of constant size
