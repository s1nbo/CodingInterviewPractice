class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        # base case
        if(len(nums) == 1):
            return [nums.copy()]

        
        for _ in range(len(nums)):
            first = nums.pop(0)
            perms = self.permute(nums)
            for j in perms:
                j.append(first)
            
            nums.append(first)
            ans.extend(perms)

        return ans


"""
Input: list of integers
Output: list of list of integers

Base case: if len(nums) == 1, return [nums]

Iterate through nums
Pop the first element and store it in a variable
Recursively call permute on the remaining elements
For each permutation, append the first element to the end
Append the permutation to the answer
Append the first element back to the end of nums

Return the answer

Example:
[1, 2, 3]
first = 1
perms = [[2, 3], [3, 2]]
perms = [[2, 3, 1], [3, 2, 1]]
ans = [[2, 3, 1], [3, 2, 1]]

first = 2
perms = [[3, 1], [1, 3]]
perms = [[3, 1, 2], [1, 3, 2]]
ans = [[2, 3, 1], [3, 2, 1], [3, 1, 2], [1, 3, 2]]

first = 3
perms = [[1, 2], [2, 1]]
perms = [[1, 2, 3], [2, 1, 3]]
ans = [[2, 3, 1], [3, 2, 1], [3, 1, 2], [1, 3, 2], [1, 2, 3], [2, 1, 3]]

Time complexity: O(n!)
Space complexity: O(n!)
"""