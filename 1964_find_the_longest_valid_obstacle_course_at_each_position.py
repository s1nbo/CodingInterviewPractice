import bisect
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        dp = []
        ans = []

        for obstacle in obstacles:
            index = bisect.bisect_right(dp, obstacle)

            if index < len(dp):
                dp[index] = obstacle
            else:
                dp.append(obstacle)
            
            ans.append(index+1)
        
        return ans


"""
Input: list of integers
Output: list of integers

Create a list to store the longest obstacle course at each position.

For each obstacle, find the index of the first value in the list that is greater than the obstacle.
If the index is less than the length of the list, replace the value at that index with the obstacle.
Otherwise, append the obstacle to the list.

Add the index of the obstacle to the answer list + 1 (since the index starts at 0).

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""