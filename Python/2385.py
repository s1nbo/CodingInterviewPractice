from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: [TreeNode], start: int) -> int:
        adjacency = defaultdict(list)
        queue = [root]
        
        while queue:
            cur = queue.pop(0)

            if cur.left:
                adjacency[cur.val].append(cur.left.val)
                queue.append(cur.left)
                adjacency[cur.left.val].append(cur.val)

            if cur.right:
                adjacency[cur.val].append(cur.right.val)
                queue.append(cur.right)
                adjacency[cur.right.val].append(cur.val)
            
        
        time = 0
        queue = [(start, time)]
        visited = set()
        visited.add(start)
        
        while queue:
            cur, time = queue.pop(0)
            for new in adjacency[cur]:
                if new not in visited:
                    queue.append((new, time+1))
                    visited.add(new)

        return time
    
# Topic: BFS, Graph Theory
# Time Complexity: O(n)
# Space Complexity: O(n)