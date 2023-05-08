class Solution:
    def numSubseq(self, nums, target: int) -> int:
        nums.sort()
        result = 0
        mod = 10 ** 9 + 7
        right = len(nums) - 1
        
        for left in range(len(nums)):
            
            while nums[right] +  nums[left] > target and left <= right:
                right -= 1
            
            if left <= right:
                result += 2 ** (right-left)

        return result % mod


"""
Input: list of integers, integer
Output: integer

We sort the list of integers since we always look for min and max during the process.
We initialize result, mod and a right pointer.

We iterate through the list of integers with a left pointer.
If the sum of the left and right pointer is greater than the target, we decrement the right pointer. (We are currently to big)

If the left pointer is less than or equal to the right pointer, we add 2 ** (right-left) to the result. 
(We are currently in the range (min = left, max = right and min + max <= target))

We return the result % mod.
 
Time Complexity: O(nlogn) due to sorting
Space Complexity: O(1)
"""