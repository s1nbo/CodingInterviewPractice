from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            happiness[i] -= i
            if happiness[i] < 0:
                break
            ans += happiness[i]
        return ans

# Topic: Sorting
# Time Complexity: O(nlogn)
# Space Complexity: O(1)