from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        nums_count = Counter(nums)
        ans = 0
        current_max = 0

        for value in nums_count.values():
            if value > current_max:
                current_max = value
                ans = value
            elif value == current_max:
                ans += value

        return ans

# Topic: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)