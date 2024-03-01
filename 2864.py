class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "1" * (s.count('1')-1) + "0" * s.count('0') + "1"

# Topic: String Manipulation / Hash Table / Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)