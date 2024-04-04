class Solution:
    def maxDepth(self, s: str) -> int:
        cur = ans = 0
        for i in s:
            if i == '(':
                cur += 1
                ans = max(cur, ans)
            elif i == ')': cur -= 1
        
        return ans

# Topic: String
# Time Complexity: O(n)
# Space Complexity: O(1)