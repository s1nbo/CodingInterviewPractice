class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        appeared = {} # Stores values that appeared int -> Bool
        
        
        for i in nums:
            if i in appeared:
                return True
            else:
                appeared[i] = True
        
        return False
                
"""
Input: array of integers

This code uses a Hashmap or Dictonary to store the values that appeared with type Integer -> Boolean.
It iterates through the list and checks if the value is in the dictionary.
If it is, it returns True.
If it is not, it adds the value to the dictionary and continues.
If no value appeares twice in nums it returns False.

Time Complexity: O(n)
Space Complexity: O(n)
"""                
