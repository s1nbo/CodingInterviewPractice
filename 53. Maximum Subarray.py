class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        result = nums[0]
        
        
        if len(nums) == 1:
            return result
        
        total = 0
        for i in nums:
            total += i
            result = max(result, total)
            
            if total < 0:
                total = 0
        
        return result

"""
Input: array of integers
Output: maximum sum of a subarray

If length of array is 1, return the first element.

Go through the array and keep track of the current sum.
If the current sum is greater than the current max, update the max.
If the current sum is negative reset the sum to 0.

Time Complexity: O(n)
Space Complexity: O(1)
"""
