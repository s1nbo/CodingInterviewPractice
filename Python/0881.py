from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = 0
        right = len(people)-1
        ans = 0

        people.sort()

        while left <= right:
            if people[left]+people[right] <= limit:
                left += 1
            right -= 1
            ans += 1

        return ans