from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def dfs(self, root, val, depth):
        if root == None:
            return
        if depth > 2:
            self.dfs(root.left, val, depth-1)
            self.dfs(root.right, val, depth-1)
        else:
            temp = root.left
            root.left = TreeNode(val, temp, None)

            temp = root.right
            root.right = TreeNode(val, None, temp)



    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            temp = TreeNode(val, root, None)
            return temp

        self.dfs(root, val, depth)

        return root

# Topic: Tree, DFS
# Time complexity: O(n)
# Space complexity: O(n)