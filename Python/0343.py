class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n-1
        exp = n//3
        match n%3:
            case 0:
                return 3 ** exp
            case 1:
                return 3 ** (exp-1) * 4
            case 2:
                return 3 ** exp * 2

# Time Complexity: O(log(n))
# Space Complexity: O(1)