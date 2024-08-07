class Solution:
    def numberToWords(self, num: int) -> str:
        nums = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        temp = 1_000_000 <= num
        temp2 = 1_000_000_000 <= num
        if num == 0:
            return "Zero"
        if num < 20:
            return nums[num]


        stack = []
        while num > 0:
            stack.append(num % 1000)
            num //= 1000
        stack.reverse()
        ans = ""

        for i in range(len(stack)):
            temp3 = stack[i]
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
            if len(stack) - i == 3:
                if temp3 == 0 and temp2:
                    continue 
                ans += "Million "
            if len(stack) - i == 2:
                if temp3 == 0 and temp:
                    continue 
                ans += "Thousand "

        return ans[:-1]

# Topic: Math, Stack
# Time Complexity: O(1), since the input is always 32-bit integer
# Space Complexity: O(1), 