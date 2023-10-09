class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def binarySearch(nums, target, left_bias):
            left, right = 0, len(nums)-1
            ans = -1 # default case

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid-1
                else:
                    ans = mid
                    if left_bias:
                        right = mid-1
                    else:
                        left = mid+1
               
            return ans

        return [binarySearch(nums, target, True), binarySearch(nums, target, False)]

# Time complexity: O(logn)
# Space complexity: O(1)
        