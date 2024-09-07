from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node, cur):
        if not cur:
            return True
        if not node or node.val != cur.val:
            return False

        return self.dfs(node.left, cur.next) or self.dfs(node.right, cur.next)
        
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.dfs(root, head): return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


# Topic: dfs, tree, linked list
# Time Complexity: O(n * m)
# Space Complexity: O(h) h is the height of the tree