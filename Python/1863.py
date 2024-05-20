from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(i, ans):
            if i == len(nums): return ans
            return dfs(i+1, ans^nums[i]) + dfs(i+1, ans)
               
        return dfs(0, 0)

# Topic: Dfs, Bit Manipulation
# Time Complexity: O(2^n)
# Space Complexity: O(n)