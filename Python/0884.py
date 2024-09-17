from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_count = Counter(s1.split() + s2.split())

        ans = []
        for w in word_count:
            if word_count[w] == 1:
                ans.append(w)

        return ans

# Topic: Hashmap
# Time Complexity: O(n)
# Space Complexity: O(n)