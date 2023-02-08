class Solution:
    def jump(self, nums: List[int]) -> int:
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


"""
Input: list of integers
Output: integer

We create a counter, left, and right.

We iterate while right is less than the length of the list minus 1.
We create a variable to store the farthest jump.
We iterate through the list from left to right plus 1.
We update farthest_jump to the maximum of farthest_jump and i plus nums[i].

We update left to right plus 1.
We update right to farthest_jump.
We increment counter.

We return counter.

This solution is a greedy algorithm. We iterate through the list and keep track of the farthest jump we can make.
We update left and right to the next range of jumps we can make. We increment counter.
left and right are the range of jumps we can make. We iterate through the list from left to right plus 1.

Time Complexity: O(n)
Space Complexity: O(1)
"""