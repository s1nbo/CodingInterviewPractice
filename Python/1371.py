class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Count, First index, Last idnex
        vowels = 'aeiou'
        ans = 0
        mask = 0
        mask_to_idx ={0: -1}

        for idx, c in enumerate(s):
            if c in vowels:
                mask ^= ord(c)-ord('a') + 1
            if mask in mask_to_idx:
                ans = max(ans, idx-mask_to_idx[mask])
            else:
                mask_to_idx[mask] = idx
        
        return ans

# Topic: Bit Manipulation
# Time complexity: O(n)
# Space complexity: O(1)