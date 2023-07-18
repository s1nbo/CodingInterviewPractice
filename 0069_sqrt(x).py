class Solution:
    def mySqrt(self, x: int) -> int:
        if not(x): 
            return x

        l, r = 1, x
        while l <= r:
            m = (l+r) // 2
            if m == x // m:
                return m
            elif m > x // m:
                r = m-1
            else:
                l = m+1
              
        return r


"""
Input: integer
Output: integer

If x is 0, we return 0.

We use binary search to find the square root of x.
Since we only need the integer part, we return r.

The idea is that sqrt(x) is between 1 and x.
if m^2 > x, then sqrt(x) is between 1 and m-1.
if m^2 < x, then sqrt(x) is between m+1 and x.
if m^2 == x, then m is the square root of x.
m^2 == x is the same as m == x // m. (Just faster?)

Time Complexity: O(log n)
Space Complexity: O(1)
"""