class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i]+i >= target:
                target = i
        
        if target == 0:
            return True
        
        return False


"""
Input: array of integers
Output: boolean

Target is the last index of the array.

Go through the array backwards.
If you can reach the target at the current index + the current element,
Update the target to be the current index.

If the target is 0 at the end of the loop, you can reach the end of the array through jumping.

Time Complexity: O(n)
Space Complexity: O(1)
"""