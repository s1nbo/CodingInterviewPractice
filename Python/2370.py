class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0]*26
        a = ord('a')
        for char in s:
            cur = ord(char)-a
            start = max(cur-k, 0)
            end = min(cur+k, 25) + 1
            dp[cur] = max(dp[start:end])+1

        return max(dp)

# Topic: Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(1)