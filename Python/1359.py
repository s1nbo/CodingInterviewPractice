class Solution:
    def countOrders(self, n: int) -> int:
        slots = 2 * n
        ans = 1
        while slots > 0:
            valid_choices = slots * (slots - 1) // 2
            ans *= valid_choices
            slots -= 2
        return ans % (10**9 + 7)


"""
Input: Integer
Output: Integer

First we need to find the total number of slots. We can do this by multiplying n by 2.
For each two slots we have, we have two choices. We can either pick up or deliver.
We can find the total number of choices by multiplying the number of slots by the number of slots - 1 and dividing by 2.
We can then multiply the total number of choices by the number of valid choices.
We can then subtract 2 from the number of slots.
We can then repeat the process until we have no more slots.

Time Complexity: O(n)
Space Complexity: O(1)
"""