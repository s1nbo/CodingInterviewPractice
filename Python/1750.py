class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s)-1

        while left < right and s[left] == s[right]:
            cur = s[left]
            while left <= right and cur == s[left]:
                left += 1
            while left <= right and cur == s[right]:
                right -= 1

        return right-left+1

# Topic: Two pointers
# Time complexity: O(n)
# Space complexity: O(1)