class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        last_used = -1
        while n > 0:
            i = 0
            
            while n - 3 ** (i+1) >= 0:
                i += 1

            if i == last_used:
                return False
            
            n -= (3 ** i)
            last_used = i
            
        return True


"""
Input: integer
Output: boolean

We iterate through the powers of 3 until we find the largest power of 3 that is less than or equal to n.
We subtract that power of 3 from n.
We repeat until n is 0.

If we ever use the same power of 3 twice, we return False.
Otherwise, we return True.

Time Complexity: O(log(n))
Space Complexity: O(1)
"""