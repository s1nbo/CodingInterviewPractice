class Solution:
    def check(self, nums: list[int]) -> bool:
        rotation = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                rotation += 1
            if rotation > 1:
                return False
        return True

# Topic: Array, Count around the corner
# Time Comeplexity: O(n)
# Space Complexity: O(1)