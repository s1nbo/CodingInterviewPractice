class Solution:
    def trap(self, height: list[int]) -> int:
        left_max = [0]
        right_max = [0]
        ans = 0
        cur_left_max = height[0]
        cur_right_max = height[-1]

        for i in range(1, len(height)):
            left_max.append(cur_left_max)
            cur_left_max = max(cur_left_max, height[i])
  
        for i in range(len(height)-2, -1, -1):
            right_max.append(cur_right_max)
            cur_right_max = max(cur_right_max, height[i])

        right_max.reverse()

        for i in range(len(height)):
            cur = min(left_max[i], right_max[i]) - height[i]
            if cur > 0: ans += cur
        
        return ans

# Topic: Array
# Time Complexity: O(n)
# Space Complexity: O(n)