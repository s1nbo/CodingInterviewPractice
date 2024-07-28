from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        count = 26
        graph = [[float("inf")]*count for _ in range(count)]
        ans = 0

        # Build graph
        for i in range(count):
            graph[i][i] = 0
            for i in range(len(cost)):
                start = ord(original[i]) - ord('a')
                end = ord(changed[i]) - ord('a')
                graph[start][end] = min(cost[i], graph[start][end])

        # Floyd-Warshall
        for k in range(count):
            for i in range(count):
                for j in range(count):
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

        # Get costs
        for i in range(len(source)):
            start = ord(source[i]) - ord('a')
            end = ord(target[i]) - ord('a')
            temp = graph[start][end]

            if temp == float('inf'):
                return -1
            
            ans += temp

        
        return ans

# Topic: Floyd-Warshall
# Time Complexity: O(source+original+26^3) = O(n) (n = source+original)
# Space Complexity: O(26^2) = O(1)



        