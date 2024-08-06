class Solution:
    def minimumPushes(self, word: str) -> int:
        count = [0]*26
        for c in word:
            count[ord(c)-ord('a')] += 1
        count.sort(reverse=True)
        
        ans = 0
        for i in range(len(count)):
            ans += count[i]*(i//8+1)
          
        return ans

# Topic: Greedy
# Time complexity: O(n log n)
# Space complexity: O(n)