from collections import defaultdict
from typing import List
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        
        if len(s) == 0 or len(s) == 1:
            return len(s)

        if len(set(s)) == 1:
            a = []
            for x in points:
                if len(a) < 2:
                    a.append([abs(x[0]), abs(x[1])])
                else:
                    if min(abs(x[0]), abs(x[1])) < min(a[0][0], a[0][1]):
                        a[0] = [abs(x[0]), abs(x[1])]
                    elif min(abs(x[0]), abs(x[1])) < min(a[1][0], a[1][1]):
                        a[1] = [abs(x[0]), abs(x[1])]
     
            if max(a[0]) == max(a[1]):
                return 0

            return 1

        letter_to_points = defaultdict(list)
        for i in range(len(points)):
            letter_to_points[s[i]].append(max(abs(points[i][0]), abs(points[i][1])))
        
        max_value = float("inf")
        for key in letter_to_points:

            if len(letter_to_points[key]) > 1:
                letter_to_points[key].sort()
                max_value = min(max_value, letter_to_points[key][1])
            
        max_value -= 1
        ans = 0

        for x in points:
            if max(abs(x[0]), abs(x[1])) <= max_value:
                ans += 1 
        
        return ans

# Topic: Hash Table
# Time complexity: O(n)
# Space complexity: O(n)
