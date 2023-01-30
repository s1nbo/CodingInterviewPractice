class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        left, right = 0, 1
        
        while right < len(prices):            
            
            current_profit = prices[right]-prices[left]
            max_profit = max(max_profit, current_profit)
            
            if prices[right] < prices[left]:
                left = right
            
            right += 1
            
        return max_profit


"""
Input: array of integers
Output: integer

First we initialize the max_profit to 0 and the left and right pointers to 0 and 1.

We loop through the array with the right pointer.
We calculate the current profit by subtracting the left pointer from the right pointer.
We update the max_profit if the current profit is greater than the current max_profit.

If the prices[right] is less than prices[left], we update the left pointer to be the right pointer.
Since the left pointer should always be the index of the lowest price we have seen so far. 
In future comparisons, we want to buy at the new lowest price.

Time Complexity: O(n)
Space Complexity: O(1)
"""