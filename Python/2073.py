from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k] 
        ans = 0
        for i in range(k+1):
            ans += min(target, tickets[i])
        target -= 1
        for i in range(k+1, len(tickets)):
            ans += min(target, tickets[i])

        return ans

# Topic: Array
# Time Complexity: O(n)
# Space Complexity: O(1)