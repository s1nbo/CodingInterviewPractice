# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        # 1
        start = ListNode(None, head)
        # 2
        cur, prev = head, start
        for i in range(left-1):
            prev, cur = cur, cur.next
        
        # 3
        prev2 = None
        for i in range(right - left+1):
            cur.next, prev2, cur = prev2, cur, cur.next

        # 4
        prev.next.next = cur
        # 5
        prev.next = prev2

        return start.next
        

"""
Input: Linked List, 2 integers
Output: Linked List

1. First we create a dummy node and set it infront of the head

2. Then we iterate through the linked list until we reach the left index
We safe the previous node and the current node

3. Then we iterate through the linked list until we reach the right index
While iterating we reverse the linked list
From  <- x  y -> z -> (with cur = y and prev2 = x)
To    <- x <- y  z -> (with cur = z and prev2 = y)

4. Then we set the node before the left index to the last node of the reversed linked list
Example: 1 -> 2 -> 3 -> 4 -> 5
left = 2, right = 4
prev = 1, cur = 5
Node 2 now points to node 5

5. And we set the last node of the reversed linked list to the node after the right index
Example: 1 -> 2 -> 3 -> 4 -> 5
left = 2, right = 4
prev = 1, prev2 = 4
Node 1 now points to node 4

Time complexity: O(n)
Space complexity: O(1)
"""
