from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root) -> List[int]:
        if not root: return []
        ans = []

        def dfs(node):
            for child in node.children:
                dfs(child)
            ans.append(node.val)

        dfs(root)
        return ans

# Topic: Tree, DFS
# Time complexity: O(n)
# Space complexity: O(n)