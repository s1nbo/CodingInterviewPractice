class Solution:
    def longestConsecutive(self, nums) -> int:
        nums = set(nums)
        max_length = 0

        for current in nums:
            
            if current-1 not in nums:
                current_length = 1

                while (current + current_length) in nums:
                    current_length += 1
                
                max_length = max(max_length, current_length)
        

        return max_length


"""
Input: List of integers
Output: Integer

We convert the list to a set. This takes O(n) time and O(n) space. 
But it allows us to check if a number is in the set in O(1) time.

We iterate through the set.
If the current number - 1 is not in the set, we know that the current number is the first number of a sequence.
We iterate through the set until we find a number that is not in the set. (This ends the sequence.)
We update the max length.

We return the max length.

Time Complexity: O(n)
Space Complexity: O(n)
"""