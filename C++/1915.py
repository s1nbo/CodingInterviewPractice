class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        ans = 0
        prefix_xor = 0
        count[0] = 1

        for char in word:
            char_idx = ord(char) - ord('a')
            prefix_xor ^= 1 << char_idx
            ans += count[prefix_xor]
            for i in range(10):
                ans += count[prefix_xor ^(1 << i)]
            count[prefix_xor] += 1

        return ans

# Topic: Bit Manipulation
# Time Complexity: O(n)
# Space Complexity: O(1)