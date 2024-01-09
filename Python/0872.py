# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sequence(self, cur, ans):
        if not cur:
            return [None]
        elif not cur.left and not cur.right:
            ans.append(cur.val)
        else:
            self.sequence(cur.left, ans)
            self.sequence(cur.right, ans)
        return ans
        
    def leafSimilar(self, root1: [TreeNode], root2: [TreeNode]) -> bool:
        return self.sequence(root1, []) == self.sequence(root2, [])

# Topics: Tree, DFS
# Time Complexity: O(n)
# Space Complexity: O(n)