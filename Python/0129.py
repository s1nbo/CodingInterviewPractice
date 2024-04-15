from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, path):
            if not node:
                return 0
            new_path = path + [node.val]
            ans = 0
            
            if not node.left and not node.right:
                return int("".join(map(str, new_path)))

            ans += helper(node.left, new_path)
            ans += helper(node.right, new_path)
        
            return ans

        return helper(root, [])

# Topic: Tree, DFS
# Time Complexity: O(n)
# Space Complexity: O(n)
