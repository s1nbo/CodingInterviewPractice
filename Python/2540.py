class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        first = 0
        second = 0

        while first < len(nums1) and second < len(nums2):
            if nums1[first] == nums2[second]:
                return nums1[first]
            elif nums1[first] > nums2[second]:
                second += 1
            else:
                first += 1
            
        return -1

# Topic: Two Pointers
# Time Complexity: O(n + m)
# Space Complexity: O(1)