class Solution:
    def isValid(self, s: str) -> bool:
 
        if len(s) % 2 != 0:
            return False
        
        stack = []
        
        for n in s:
            if n == '(' or n == '[' or n == '{':
                stack.append(n)
            else:
                if len(stack) == 0:
                    return False
                else:
                    current = stack.pop()
                    if (n == ')' and current == '(') \
                    or (n == ']' and current == '[') \
                    or (n == '}' and current == '{'):
                        continue
                    else:
                        return False
    
        return not stack


"""
Input: string
Output: boolean

We want to check if the brackets are balanced.
If the length of the string is odd, then it is not balanced.

We start by creating a stack.
We iterate through the string and push every opening brackets onto the stack.
If we encounter a closing bracket, we pop the last element off the stack and check if it matches the current bracket.
If it does not, then the brackets are not balanced.

If we reach the end of the string and the stack is empty, then the brackets are balanced.

Time Complexity: O(n)
Space Complexity: O(n)
"""
        