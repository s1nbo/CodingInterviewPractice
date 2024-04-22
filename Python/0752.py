from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        set_deadends = set(deadends)
        
        if "0000" in set_deadends:
            return -1

        visited = set("0000")

        queue = deque([])
        queue.append(("0000", 0))

        while queue:
            cur, moves = queue.popleft()

            if cur == target:
                return moves

            for i in range(4):
                for change in [-1, 1]:
                    new = (int(cur[i]) + change) % 10
                    temp = cur[:i] + str(new) + cur[i+1:]
            
                    if temp not in visited and temp not in set_deadends:
                        visited.add(temp)
                        queue.append((temp, moves+1))

        return -1

# Topic: BFS
# Time Complexity: O(1)
# Space Complexity: O(1)