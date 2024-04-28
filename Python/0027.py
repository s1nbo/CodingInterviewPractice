from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1
        
        return pointer

# Topic: Array
# Time complexity: O(n)
# Space complexity: O(1)