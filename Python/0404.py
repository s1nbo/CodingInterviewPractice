from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node, pos):
            cur = 0
            if node == None:
                return cur
            elif node.left == None and node.right == None and pos:
                return cur + node.val

            if node.left:
                cur += helper(node.left, True)
            if node.right:
                cur += helper(node.right, False)
             
            return cur

        return helper(root, False)

# Topic: Tree, Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)