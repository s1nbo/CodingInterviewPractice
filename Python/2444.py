class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        ans = 0
        cur_min = -1
        cur_max = -1
        invalid = -1

        for r in range(len(nums)):
            if nums[r] == minK:
                cur_min = r
            if nums[r] == maxK:
                cur_max = r
            if nums[r] < minK or nums[r] > maxK:
                invalid = r
            
            ans += max(0, min(cur_max, cur_min)-invalid)

        return ans