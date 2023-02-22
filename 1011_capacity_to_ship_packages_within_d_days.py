class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        low = max(weights) # lower bound
        high = sum(weights) # upper bound
        
        result = high

        def days_needed(mid):
            ships, current = 1, mid
            for w in weights:
                if current - w < 0:
                    ships += 1
                    current = mid
                current -= w
            return ships <= days

        # binary search
        while low <= high:
            mid = (low + high) // 2
            if days_needed(mid):
                result = min(result, mid)
                high = mid - 1
            else:
                low = mid + 1
        return result


"""
Input: array of ints and int
Output: int

first we set the lower bound to the max of the weights
and the upper bound to the sum of the weights

we then use binary search to find the minimum capacity
that can ship all the weights in the given number of days

we use a helper function to check if a given capacity can ship all the weights in the given number of days

If the current capacity can ship all the weights in the given number of days, we update the result and set the upper bound to the mid - 1
If the current capacity cannot ship all the weights in the given number of days, we set the lower bound to the mid + 1
Unitl the lower bound is greater than the upper bound

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""
        


