class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:
            while k > 0 and stack and stack[-1] > char:
                k -= 1
                stack.pop()
            if(stack or char != "0"): stack.append(char)
            
        stack = stack[:len(stack)-k]

        ans = "".join(stack)

        return ans if ans else "0"
            
