class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low, res = prices[0], 0
        for cur in prices:
            if cur < low:
                low = cur
            else:
                res = max(res, cur-low)
        return res 
            
"""
Input: array of integers
Output: integer

First we initialize the lowest value and the result variable.
We loop through the array.
If the current value is less than the lowest value, we update the lowest value.
Otherwise, we update the result variable by comparing the result
with the current value minus the lowest value.
we return the result variable.

Time Complexity: O(n)
Space Complexity: O(1)
"""