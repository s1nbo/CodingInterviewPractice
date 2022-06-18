class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {} # integer in nums -> frequency
        result = [[]]*(len(nums)+1)
        return_value = []
        

        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                 frequency[i] = 1
        

        for j in frequency:
            result[frequency[j]] = result[frequency[j]] + [j]


        for i in range(len(result)-1, -1, -1):
            if result[i] != []:
                return_value = return_value + result[i]
                if len(return_value) == k:
                    return return_value


"""
Input: list of integers, integer
Output: list of integers

Return the top k frequent integers in the list nums.

(frequency)
Count the frequency of each integer in nums and store it in a dictionary.
Key: integer in nums, Value: frequency of integer in nums.

(result)
Convert the dictionary to a list of lists.
The index of the list is the frequency of the integer.
The value of the list is a list of integers with that frequency.


(return_value)
Go through the list of lists backwards and add the lists to the return list.
If the return_value is already k elements long, return it.

There is always a unique solution.

Time Complexity: O(n)
Space Complexity: O(n)
"""
                
        