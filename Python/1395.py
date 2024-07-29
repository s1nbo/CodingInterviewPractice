from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:

        ans = 0
        n = len(rating)

        # i is the middle element of the triplet
        for i in range(n):

            left_less_counter = 0
            left_greater_counter = 0
            right_less_counter = 0
            right_greater_counter = 0

            for j in range(i):
                left_less_counter += rating[i] > rating[j]
                left_greater_counter += rating[i] < rating[j]
            
            for j in range(i+1, n):
                right_less_counter += rating[i] > rating[j]
                right_greater_counter += rating[i] < rating[j]
            
            ans += left_less_counter*right_greater_counter + left_greater_counter*right_less_counter
    
        return ans

# Topic: Array
# Time complexity: O(n^2), O(nlogn) is also possible
# Space complexity: O(1)