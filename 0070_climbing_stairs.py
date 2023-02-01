class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n-1):
            temp = one
            one += two
            two = temp
        
        return one


"""
Input: integer
Output: integer

We start with one and two steps. 
We iterate through the number of steps minus one.

We create a temporary variable to hold the value of one.
We add one and two and assign it to one.
We assign two to the temporary variable.

We return one.

This is a fibonacci sequence.

Time Complexity: O(n)
Space Complexity: O(1)
"""