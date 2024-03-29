class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        target = max(nums)
        counter = 0
        ans = 0
        l = 0
        
        for r in range(len(nums)):
            if nums[r] == target:
                counter += 1

            while (counter > k or (counter == k and nums[l] != target)) and l <= r:
                if nums[l] == target:
                    counter -= 1
                l += 1

            if counter == k:
                ans += l+1

        return ans
        