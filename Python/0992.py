from dict import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        val_freq = defaultdict(int)
        ans = 0
        l_near = 0
        l_far = 0
        for r in range(len(nums)):
            val_freq[nums[r]] += 1

            while len(val_freq) > k:
                val_freq[nums[l_near]] -= 1
                if val_freq[nums[l_near]] == 0:
                    del val_freq[nums[l_near]]
                l_near += 1
                l_far = l_near

            while val_freq[nums[l_near]] > 1:
                val_freq[nums[l_near]] -= 1
                l_near += 1

            if len(val_freq) == k:
                ans += l_near - l_far + 1

        return ans 

# Topic: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(n)