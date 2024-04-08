from typing import List
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ans = len(students)
        count = Counter(students)

        for s in sandwiches:
            if count[s] == 0:
                break
            count[sandwiches[0]] -= 1
            ans -= 1

        return ans

# Topic: Array
# Time Complexity: O(n)
# Space Complexity: O(1)