class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        indexA, indexB = 0, len(numbers)-1
        
        while True:
            current = numbers[indexA] + numbers[indexB]
            if current > target:
                indexB -= 1
            elif current < target:
                indexA += 1
            else:
                return [indexA+1, indexB+1]


"""
Input: array of integers (sorted), target integer
Output: two indexes+1 of the two integers that sum to the target

start at the beginning and end of the array
if the sum of the two numbers is greater than the target, move the end pointer to the left
if the sum of the two numbers is less than the target, move the start pointer to the right
if the sum of the two numbers is equal to the target, return the indexes+1

Time Complexity: O(n)
Space Complexity: O(1)
"""