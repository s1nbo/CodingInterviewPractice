class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        l, r = 0, len(arr)-1

        while l <= r:
            m = (l+r) // 2

            if arr[m+1] > arr[m]:
                l = m+1
            elif arr[m-1] > arr[m]:
                r = m-1
            else:
                return m


"""
Input: list of integers
Output: integer

Binary search
We are looking for the peak of the mountain
We can use binary search to find the peak
We can compare the middle element with the element to the right
If the element to the right is greater than the middle element, then we know that the peak is to the right
If the element to the left is greater than the middle element, then we know that the peak is to the left
If the middle element is greater than both the element to the left and the element to the right, then we know that the middle element is the peak

Time Complexity: O(logn)
Space Complexity: O(1)
"""