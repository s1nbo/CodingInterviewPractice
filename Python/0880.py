class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack_length = 0
        for char in s:
            if char.isdigit():
                stack_length *= int(char)
            else:
                stack_length +=1
        for idx in range(len(s)-1, -1, -1):
            current = s[idx]

            if current.isdigit():
                stack_length //= int(current)
                k %= stack_length
            else:
                if k == 0 or stack_length == k:
                    return current
            
                stack_length -= 1

        return ""

