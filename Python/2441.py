from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = -1
        for cur in nums_set:
            if -cur in nums_set:
                ans = max(ans, cur)
        return ans


# Topic: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)