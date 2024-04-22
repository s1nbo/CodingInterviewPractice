# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ans = 0
    def dfs(self, node, ans):
        if not node:
            return float('inf'), -1

        left = self.dfs(node.left,  ans)
        right = self.dfs(node.right, ans)

        minimum = min(node.val, left[0], right[0])
        maximum =  max(node.val, left[1], right[1])
        self.ans = max(self.ans, abs(minimum - node.val), abs(maximum - node.val))
        return minimum, maximum

    def maxAncestorDiff(self, root: list[TreeNode]) -> int:
        self.dfs(root, self.ans)
        return self.ans


# Topic: Tree, DFS
# Time Complexity: O(n)
# Space Complexity: O(h) h is the height of the tree
            