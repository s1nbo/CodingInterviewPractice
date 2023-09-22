from statistics import median

class Solution: 
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if nums1 == []:
            return median(nums2)
        elif nums2 == []:
            return median(nums1)
        
        total_length = len(nums1) + len(nums2)
        pos1 = 0
        pos2 = 0
        merged = []

        while len(merged) <= total_length // 2:
            if nums1[pos1] < nums2[pos2]:
                merged.append(nums1[pos1])
                pos1 += 1
                if pos1 == len(nums1):
                    while len(merged) <= total_length // 2:
                        merged.append(nums2[pos2])
                        pos2 += 1
            else:
                merged.append(nums2[pos2])
                pos2 += 1
                if pos2 == len(nums2):
                    while len(merged) <= total_length // 2:
                        merged.append(nums1[pos1])
                        pos1 += 1

        if total_length % 2 == 1:
            return merged[-1]
        else:
            return (merged[-1] + merged[-2]) / 2 
