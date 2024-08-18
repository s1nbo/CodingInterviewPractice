class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2, i3, i5 = 0,0,0

        for _ in range(1, n):
            next_num = min(nums[i2]*2, nums[i3]*3, nums[i5]*5)
            nums.append(next_num)
            
            i2 += next_num == nums[i2]*2
            i3 += next_num == nums[i3]*3
            i5 += next_num == nums[i5]*5
                
        return nums[n-1]

# Topics: Dynamic Programming
# Time complexity: O(n)
# Space complexity: O(n)