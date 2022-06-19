class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        solution = [1]*len(nums)
        
        current = 1
        for i in range(len(nums)):
            solution[i] *= current
            current *= nums[i]
        
        current = 1
        for j in range(len(nums)-1, -1, -1):
            solution[j] *= current
            current *= nums[j]
        
        return solution
        
        
"""
Input: list of integers
Output: list of integers

We start by creating a result list of length nums length and setting each element to 1.

We iterate through the list and set the current value to the product of all the elements before it.
We then iterate through the list in reverse and set the current value to the product of all the elements after it.

The result list is the product of the elements before and after the current element.


Time Complexity: O(n)
Space Complexity: O(n)
"""
        