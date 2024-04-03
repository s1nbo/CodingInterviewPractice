from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        idx = 0
        while idx < len(intervals)-1:
            if intervals[idx][1] >= intervals[idx+1][0]:
                intervals[idx] = [min(intervals[idx][0], intervals[idx+1][0]), max(intervals[idx][1], intervals[idx+1][1])]
                del intervals[idx+1]
            else:
                idx += 1

        return intervals

# Topic: Array, Sort
# Time: O(nlogn)
# Space: O(1)
        