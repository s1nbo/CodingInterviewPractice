class Solution:
    def bestTeamScore(self, scores, ages) -> int:
        
        players = sorted(zip(ages, scores))
        dp = [0] * len(players)

        for i, (_, score) in enumerate(players):
            dp[i] = score
            
            for j in range(i):
                if players[j][1] <= score:
                    dp[i] = max(dp[i], dp[j] + score)

        return max(dp)


"""
Input: Two lists of integers
Output: Integer

First we zip the two lists together and sort them by age.

Then we create a dp array that will hold the max score for each player.

We iterate through the players and set the dp value to the current player's score.

Then we iterate through the players again and check if the current player's score is greater than the previous player's score.
If it is, we set the dp value to the max of the current dp value and the previous player's dp value plus the current player's score.

Finally, we return the max value in the dp array.

Type: Dynamic Programming

Time Complexity: O(n^2)
Space Complexity: O(n)
"""