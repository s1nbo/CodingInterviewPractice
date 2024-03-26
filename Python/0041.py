class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        l = len(nums)

        for i in range(l): # remove all negative numbers
            if nums[i] < 0:
                nums[i] = 0 
        
        for i in range(l):
            cur = abs(nums[i])
            if 1 <= cur <= l: # If the number interstes us
                
                if nums[cur-1] > 0:
                    nums[cur-1] *= -1 # Mark that we have the number in the array

                elif nums[cur-1] == 0: # This number does not interst us
                    nums[cur-1] = -1*(l+1)
                
        for i in range(1, l+1):
            if nums[i-1] >= 0:
                return i

        return l+1
    
# Topic: Array
# Time complexity: O(n)
# Space complexity: O(1)
