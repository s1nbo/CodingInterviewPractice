import math
from typing import List

class Solution:
    def helper(self, n: int) -> int:
        if n <= 0: 
            return 0
        ans = 0
        base = 1 # number of reductions our numbers currently need to reach zero (1,2,3, ...)
        l = 1 # 4**(base-1)
        while l <= n:
            r = l*4 - 1 # 4**base - 1
            # Every number in the range [l, r] needs 'base' operations to reach zero
            
            # How many numbers from [l, r] are <= n?
            count = min(r, n) - l + 1
            ans += count * base
            
            # Next base and range
            base += 1
            l *= 4

        return ans

    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for left, right in queries:
            total = self.helper(right) - self.helper(left-1)
            ans += math.ceil(total/2) # (total + 1) // 2 
        return ans
