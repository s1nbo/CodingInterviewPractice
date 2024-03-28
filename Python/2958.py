class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        ans = 0
        val_freq = {}
        l = 0
        for r in range(len(nums)):
            val_freq[nums[r]] = val_freq.get(nums[r], 0) + 1
           
            while l <= r and val_freq[nums[r]] > k:
                val_freq[nums[l]] -= 1
                l += 1

            ans = max(ans, r-l+1)

        return ans