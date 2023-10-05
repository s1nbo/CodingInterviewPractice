class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

# Time Complexity: O(n)
# Space Complexity: O(1)