class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        remainder_index = {} # remainder -> Index
        current_remainder = 0

        for i in range(len(nums)):
            current_remainder = (nums[i] + current_remainder) % k

            if current_remainder == 0 and i >= 1:
                return True

            if current_remainder in remainder_index:
                if i - remainder_index[current_remainder] >= 2:
                    return True
            else:
                remainder_index[current_remainder] = i
            
        return False


"""
Input: List of integers, integer
Output: boolean

We use a dictionary to store the remainder and the index.
We use a variable to store the current remainder.

We iterate through the list.
We update the current remainder.

If the current remainder is 0 and the index is greater than 1, we return True. 
This is because we have a subarray of length 2 with a remainder of 0.

If the current remainder is in the dictionary, we check if the difference between the current index and the index of the remainder is greater than 2.
If it is, we return True. This is because we have a subarray of length greater than 2 with a remainder of 0.

If the current remainder is not in the dictionary, we add it to the dictionary.

We return False.

Time Complexity: O(n)
Space Complexity: O(n)
"""