class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = s.count('a')
        b_count = 0
        ans = len(s)

        for char in s:
            a_count -= char == 'a'
            ans = min(ans, a_count+b_count) 
            b_count += char == 'b' 
        
        return ans
    
# Topic: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

"""
Core idea:
- Count the number of 'a' right of the current character
- Count the number of 'b' left of the current character
- Best answer is the minimum of the sum of the two counts
"""