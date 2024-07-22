from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        both = sorted(zip(heights, names), reverse=True)
        return [n for _, n in both]
        

# Topics: Sort
# Time Complexity: O(nlogn)
# Space Complexity: O(n)