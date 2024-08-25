from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def travel(node):
            if node == None:
                return ans
            travel(node.left)
            travel(node.right)
            ans.append(node.val)
            return ans
        
        return travel(root)

# Topics: Tree, Depth-first Search
# Time complexity: O(n)
# Space complexity: O(n)