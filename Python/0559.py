"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root) -> int:

        if root == None:
            return 0
        
        answer = 0
        for child in root.children:
            answer = max(answer, self.maxDepth(child))
        
        return answer + 1


"""
Input: root of a n-ary tree
Output: integer

We use recursion to traverse the tree.
We return 0 if the root is None.
We return the max of the depths of the children + 1.

Time Complexity: O(n)
Space Complexity: O(n)
"""