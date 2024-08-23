import re
from math import gcd
class Solution:
    def fractionAddition(self, expression: str) -> str:

        fractions = re.findall('[+-]?\d+/\d+', expression)

        numerator = 0
        denominator = 1

        for frac in fractions:
            num, denom = map(int, frac.split('/'))

            numerator = numerator * denom + num * denominator
            denominator *= denom


        common = gcd(abs(numerator), denominator)

        numerator //= common
        denominator //= common

        return f'{numerator}/{denominator}'

# Topics: Math, Regex
# Time complexity: O(n)
# Space complexity: O(1)