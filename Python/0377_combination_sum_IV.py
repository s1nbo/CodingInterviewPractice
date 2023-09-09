class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = {0:1}

        for cur in range(1, target+1):
            dp[cur] = 0
            for n in nums:
                dp[cur] += dp.get(cur - n, 0)
        
        return dp[target]


"""
Input: list of positive integers, integer
Output: integer

First we crate a dictonary to store the amount of ways to get to a certain number
We start at 0, and there is only 1 way to get to 0, which is to not use any numbers
Then we go through each number from 1 to target
For each number, we go through each number in the list
We add the amount of ways to get to the current number minus the current number
If the current number minus the current number is not in the dictonary, we add 0
We add the amount of ways to get to the current number minus the current number to the current number
We return the amount of ways to get to the target number

Time complexity: O(n * m) where n is the target and m is the length of the list
Space complexity: O(n) where n is the target
"""