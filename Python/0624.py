from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0

        smallest = arrays[0][0]
        largest = arrays[0][-1]

        for i in range(1, len(arrays)):
            temp_small = arrays[i][0]
            temp_large = arrays[i][-1]
            ans = max( ans, abs(temp_large-smallest), abs(largest-temp_small) )
            smallest = min(smallest, temp_small)
            largest = max(largest, temp_large)

        return ans

# Topics: Array, Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)