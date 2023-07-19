class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        # earliest end date next -> greedy stays ahead
        current_end = -5*10**4-1 # Lowest Number Possible
        answer = 0
        intervals.sort(key = lambda x : x[1])
        for i in range(len(intervals)):
            if current_end <= intervals[i][0]:
                current_end = intervals[i][1]
            else:
                answer += 1
        return answer


"""
Input: list of lists of integers (intervals)
Output: integer

We sort the intervals by their end date.
We keep track of the earliest end date.
If the current interval's start date is before the earliest end date,
then we have an overlap. We increment the answer.
Otherwise, we update the earliest end date to the current interval's end date.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

                    