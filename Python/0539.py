from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []

        for tp in timePoints:
            h, m = map(int, tp.split(":"))
            minutes.append(60*h + m)
        
        minutes.sort()
        ans = 60*24
        for i in range(len(minutes)-1):
            ans = min(ans, minutes[i+1]-minutes[i])

        ans = min(ans, 24*60-minutes[-1] + minutes[0])

        return ans


# Topic: Array, Sorting, String
# Time Complexity: O(nlogn)
# Space Complexity: O(n)