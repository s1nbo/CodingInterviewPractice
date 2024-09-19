class Solution:
    def jump(self, nums) -> int:
        counter = 0
        left = right = 0

        while right < len(nums)-1:
            farthest_jump = 0
            for i in range(left, right+1):
                farthest_jump = max(farthest_jump, i+nums[i])

            left = right + 1
            right = farthest_jump
            counter += 1
        
        return counter


# Topics: Array, Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)