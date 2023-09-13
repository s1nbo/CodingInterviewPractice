class Solution:
    def candy(self, ratings: list[int]) -> int:
        candy = [1]*len(ratings)
         
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = max(candy[i], candy[i-1]+1)

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1]+1)
    
        return sum(candy)
    

"""
Input: list of integers
Output: integer

First we give each child 1 candy. 
Then we iterate through the list twice, 
once from left to right and once from right to left. 
If the child to the left has a higher rating, we give the child to the right one more candy than the child to the left. 
We do the same thing for the right to left iteration. 

Then we return the sum of the candies.

Time Complexity: O(n)
Space Complexity: O(n)
"""