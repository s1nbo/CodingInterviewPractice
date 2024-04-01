class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

# Topic: String
# Time Complexity: O(n)
# Space Complexity: O(1)