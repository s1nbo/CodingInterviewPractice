class Solution:
    def eventualSafeNodes(self, graph):
        safe_node = {}
        n = len(graph)
        ans = []

        def dfs(node):
            if node in safe_node:
                return safe_node[node]
            safe_node[node] = False

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return safe_node[node]
            
            safe_node[node] = True
            return safe_node[node]
        
        for node in range(n):
            if dfs(node):
                ans.append(node)
        
        return ans


"""
Input: 2D array of graph edges (directed graph)
Output: list of nodes that are safe

We create a dictionary that will hold the nodes that are safe.
We create a list that will hold the nodes that are safe.

We create a function that will perform a depth first search on a node.
If the node is in the dictionary, we return the value of the node in the dictionary.
If not we set the value of the node in the dictionary to False.

We iterate through the neighbors of the node.
If the neighbor is not safe, we return False.
If the neighbor is safe, we continue iterating through the neighbors.

If we finish iterating through the neighbors and all the neighbors are safe, 
we set the value of the node in the dictionary to True.

We iterate through the nodes.
If the node is safe, we append it to the list of safe nodes.

We return the list of safe nodes.

Time Complexity: O(n^2) 
Space Complexity: O(n)
"""