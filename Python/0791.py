from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""
        count = Counter(s)

        for cur in order:
            if cur in count:
                ans += cur * count[cur]
                count.pop(cur)
        
        for key, value in count.items():
            ans += key * value 

        return ans

# Topic: Hash Table, String
# Time Complexity: O(n)
# Space Complexity: O(n)
