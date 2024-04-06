class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ')' and stack and stack[-1][0] == '(':
                stack.pop()
            elif s[i] == '(' or s[i] == ')':
                stack.append([s[i], i])
        
        offset = 0
        for (_, j) in stack:
            s = s[:j-offset] + s[j+1-offset:]
            offset += 1

        return s

# Topic: String, Stack
# Time Complexity: O(n)
# Space Complexity: O(n)