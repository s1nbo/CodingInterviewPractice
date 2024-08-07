class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        nums = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        isMillion = 1_000_000 > num
        isBillion = 1_000_000_000 > num

        if num < 20:
            return nums[num]


        stack = []
        while num > 0:
            stack.append(num % 1000)
            num //= 1000
        stack.reverse()
        ans = ""

        for i in range(len(stack)):
            isZero = stack[i] != 0
            if stack[i] > 99:
                ans += nums[stack[i] // 100] + " Hundred "
                stack[i] %= 100
            if stack[i] > 19:
                ans += tens[stack[i] // 10] + " "
                stack[i] %= 10
            if stack[i] > 0:
                ans += nums[stack[i]] + " "
            
            if len(stack) - i == 4:
                ans += "Billion "
            elif len(stack) - i == 3 and (isZero or isBillion): 
                ans += "Million "
            elif len(stack) - i == 2 and (isZero or isMillion):
                ans += "Thousand "

        return ans[:-1]

# Topic: Math, Stack
# Time Complexity: O(1), since the input is always 32-bit integer
# Space Complexity: O(1)