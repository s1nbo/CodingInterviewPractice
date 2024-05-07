class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        number_required = {} # Maps  n = target-num -> to index of num

        for i in range(len(nums)):
            if nums[i] in number_required: # if current value is in the dictionary we have found a solution
                return [i, number_required[nums[i]]]
            else:
                number_required[target-nums[i]] = i 
        

"""
Input: array of integers, target integer
Output: two indexes of the two integers that sum to the target

First create a dictionary to store the difference between target and current num and their indexes.
The difference is the key and the index is the value.

difference = target - num1
target = num1 + num2
=> num2 = difference 
So the difference is the second value we want to find.

Time Complexity: O(n)
Space Complexity: O(n)
"""
