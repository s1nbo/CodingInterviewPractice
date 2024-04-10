from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        ans = [0] * n
        idx = deque(range(n))
        for card in deck:
            ans[idx.popleft()] = card
            if idx:
                idx.append(idx.popleft())
                
        return ans

# Topic: Array
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
