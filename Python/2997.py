from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor, ans = 0, 0

        for i in nums: xor ^= i

        while k or xor:
            ans += ((k%2)!= (xor%2))
            k //= 2
            xor //= 2

        return ans

# Topic: Bit Manipulation
# Time Complexity: O(n)
# Space Complexity: O(1)        
        