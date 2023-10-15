class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()

        for idx, val in enumerate(nums):
            
            # Break after all negatives and zeros
            if val > 0: 
                break 
            
            # Skip dupes
            if idx > 0 and nums[idx-1] == val:
                continue
            
            l, r = idx+1, len(nums)-1

            while l < r:
                cur = nums[l] + nums[r] + val
                if cur > 0:
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    ans.append([nums[l], nums[r], val])
                    # Next solution should not use the same pointers (find a new l that is still smaller than r)
                    l += 1 
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 

        return ans

# Time Complexity: O(n^2)
# Space Complexity: O(n)