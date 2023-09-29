class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        increase = False
        decrease = False
        current = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < current:
                decrease = True
            if nums[i] > current:
                increase = True
            if increase and decrease:
                return False

            current = nums[i]

        return True

# Time complexity: O(n)
# Space complexity: O(1)