class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        l = 0
        ans = 0

        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l += 1
            char.add(s[r])
            ans = max(ans, len(char))

        return ans

# Topic: Sliding Window, Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)