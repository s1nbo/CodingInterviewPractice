class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        cur = 1
        paste = 1
        ans = 1

        while cur < n:
            if n % cur == 0 and paste != cur:
                paste = cur
            else:
                cur += paste
            ans += 1

        return ans

# Topic: Math, Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(1)