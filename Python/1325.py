# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def bfs(node):
            if node.left != None:
                if bfs(node.left):
                    node.left = None
            if node.right != None:
                if bfs(node.right):
                    node.right = None

            if node.left == None and node.right == None and target == node.val:
                return 1
            return 0

        if bfs(root): 
            return None
        return root


# Topic: Tree, DFS
# Time Complexity: O(n)
# Space Complexity: O(n)