class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        num_let = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtracking(comb, digits):
            # base case
            if not digits:
                output.append(comb)
            else:
                for current in num_let[digits[0]]: 
                     backtracking(comb + current, digits[1:]) 
               
        output = []
        if digits:
            backtracking("", digits)
        
        return output


"""
Input: String
Output: List of Strings

We initialize a dictionary, num_let, that maps a number to the letters it represents.

We define a function, backtracking, that takes in a string, comb, and a string, digits.
        If digits is empty, we append comb to output.
        Otherwise, we loop through the letters that the first digit represents.
                We call backtracking with the current letter added to comb and the rest of digits.

We initialize output to an empty list.
If digits is not empty, we call backtracking with an empty string and digits.

We return the output.

Time Complexity: O(4^n) where n is the number of digits in digits.
Space Complexity: O(4^n) where n is the number of digits in digits.
"""
    