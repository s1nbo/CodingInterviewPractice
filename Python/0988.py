from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node):
        if not node:
            return

        self.path.append(chr(node.val + ord("a")))

        if not node.left and not node.right:
            cur = "".join(self.path[::-1])
            self.ans = min(cur, self.ans)

        self.dfs(node.left)
        self.dfs(node.right)

        self.path.pop()

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = "{"
        self.path = []
        self.dfs(root)

        return self.ans

# Topic: Tree, DFS
# Time complexity: O(n)
# Space complexity: O(h) where h is the height of the tree