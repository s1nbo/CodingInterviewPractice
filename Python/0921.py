class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        o = 0
        for c in s:
            if c == '(':
                o += 1
            elif o == 0:
                ans += 1
            else:
                o -= 1
                
        return ans + o

# Topic: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)
