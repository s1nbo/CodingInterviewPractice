# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1

"""
Input: root of a binary tree
Output: integer

We use recursion to traverse the tree.
We return 0 if the root is None.
We return the max of the left and right depths + 1.

Time Complexity: O(n)
"""
