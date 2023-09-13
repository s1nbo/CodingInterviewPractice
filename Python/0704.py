class Solution:
    def search(self, nums, target):
        # Binary Search
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return m
        
        return -1


"""
Input: array of integers, integer
Output: integer

We use binary search to find the target.
If the target is not found, we return -1.

Time Complexity: O(log n)
Space Complexity: O(1)
"""