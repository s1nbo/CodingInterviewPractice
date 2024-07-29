from collections import defaultdict, deque
from typing import List

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        queue = deque([1])
        cur_time = 0
        ans = -1
        visited = defaultdict(list)
        
        # Graph
        for v, u in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                # If the target has been visited twice
                if node == n: 
                    if ans != -1:
                        return cur_time
                    ans = cur_time
                

                for neighbor in graph[node]:
                    # Each neighbour can only be added once with the same cur_time and twice in total
                    if len(visited[neighbor]) == 0 or (len(visited[neighbor]) == 1 and visited[neighbor][0] != cur_time):
                        queue.append(neighbor)
                        visited[neighbor].append(cur_time)
            
            # Red or green light
            if (cur_time // change) % 2 == 1:
                cur_time += change - (cur_time % change)
            cur_time += time 

# Topic: BFS, Graph
# Time Complexity: O(n+m), (n = n, m = len(edges))
# Space Complexity: O(n+m), (n = n, m = len(edges))