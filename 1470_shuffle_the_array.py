class Solution:
    def shuffle(self, nums: int, n: int) -> int:
        # n = len(nums) // 2
        answer = []
    
        for i in range(n):
            answer.append(nums[i])
            answer.append(nums[i + n])
    
        return answer


"""
Input: list of integers, integer
Output: list of integers

We create an empty list to store the answer.
We iterate through the first half of the list.
We append the first half of the list to the answer.
We append the second half of the list to the answer.

Time Complexity: O(n)
Space Complexity: O(n)
"""
