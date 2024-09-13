from itertools import accumulate
from operator import xor
from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr[:] = accumulate(arr, xor)
        ans = []

        for q in queries:
            if q[0] == 0:
                ans.append( arr[q[1]] )
            else:
                ans.append( arr[q[1]]^arr[q[0]-1] )

        return ans
    

# Topic: Bit Manipulation
# Time Complexity: O(n + m)
# Space Complexity: O(1)     