class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cur = 0
        while cur < len(nums):
            while cur+1 < len(nums) and nums[cur] == nums[cur+1]:
                nums.pop(cur+1)      
            cur += 1
        
        return len(nums)

# Time Complexity: O(n)
# Space Complexity: O(1)