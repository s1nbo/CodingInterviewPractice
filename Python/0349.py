class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))

# Topic: Array
# Time Complexity: O(n)
# Space Complexity: O(n)