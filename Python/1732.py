class Solution:
    def largestAltitude(self, gain) -> int:
        current, ans = 0, 0
        
        for i in gain:
            current += i
            ans = max(ans, current)

        return ans

"""
Input: List of Integers
Output: Integer

We initialize two variables, current and ans, to 0.

We loop through the list.
We add the current value to current.
We set ans to the maximum of ans and current.

We return ans.

Time Complexity: O(n)
Space Complexity: O(1)
"""
