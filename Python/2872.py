from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Graph
        g = [[] for _ in range(n)]
        for v, u in edges: 
            g[v].append(u)
            g[u].append(v)
        
        self.ans = 0

        def dfs(node, parent):
            s = values[node]
            for adj in g[node]:
                if adj != parent:
                    s += dfs(adj, node)
            
            if s%k == 0:
                self.ans += 1
            
            return s%k

        dfs(0, -1)
        
        return self.ans
        
# Time Complexity: O(n + m) where n is number of nodes and m is number of edges
# Space Complexity: O(n) for the graph representation and recursion stack

# First we create the grpah
# Then we do a DFS traversal to calculate the sum of each subtree
# If the sum of a subtree is divisible by k, we increment the answer