from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        connections = defaultdict(list)
        degree = [0] * n

        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)
            degree[a] += 1
            degree[b] += 1

        leaves = deque([i for i in range(n) if degree[i] == 1])

        remainder = n

        while remainder > 2:
            leaves_count = len(leaves)
            remainder -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in connections[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)

# Topic: Graph, BFS
# Time Complexity: O(n)
# Space Complexity: O(n)