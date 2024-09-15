from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans, cur = 0, 0
        target = max(nums)

        for i in nums:
            if i == target:
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 0
        
        return max(ans, cur)


# Topic: Array
# Time complexity: O(n)
# Space complexity: O(1)