class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = start ^ goal
        return bin(result).count('1')

# Topic: Bit Manipulation
# Time Complexity: O(k) where k is the number of bits
# Space Complexity: O(1)