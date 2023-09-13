class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - (purchaseAmount+5) // 10 * 10


"""
Input: Integer
Output: Integer

Find the closest multiple of 10 to the purchase amount

Time Complexity: O(1)
Space Complexity: O(1)
"""