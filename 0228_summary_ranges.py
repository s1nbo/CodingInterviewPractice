class Solution:
    def summaryRanges(self, nums):
        if nums == []: return [] # Corner case
        ans, i = [], 0
        while i+1 < len(nums):
            if nums[i]+1 == nums[i+1]: # Multiple digits
                for j in range(i+1, len(nums)):
                    if j+1 >= len(nums):
                        ans.append(f"{nums[i]}->{nums[j]}")
                        return ans
                    elif nums[j]+1 != nums[j+1]:
                        ans.append(f"{nums[i]}->{nums[j]}")
                        break 
                i = j
            
            else: # Single digit
                ans.append(f"{nums[i]}")
        
            i += 1
        
        ans.append(f"{nums[i]}")
        return ans


"""
Input: List of integers
Output: List of strings

We iterate through the list of integers and check if the next integer is consecutive.
If it is, we keep iterating until we find a non-consecutive integer.
Else we add the integer to the ans.


Time Complexity: O(n)
Space Complexity: O(n)
"""