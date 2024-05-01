class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1: return word
        return word[idx::-1] + word[idx+1:]

# Topic: String
# Time Complexity: O(n)
# Space Complexity: O(1)