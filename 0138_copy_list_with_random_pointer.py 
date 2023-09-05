# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        old_new = {None : None}
        cur = head
        while cur:
            cur_copy = Node(cur.val)
            old_new[cur] = cur_copy
            cur = cur.next
            
        cur = head
        while cur:
            copy = old_new[cur]
            copy.next = old_new[cur.next]
            copy.random = old_new[cur.random]
            cur = cur.next

        return old_new[head]
    

"""
Input: head of a linked list
Output: head of a deep copy of the linked list

We iterate through the linked list twice.
First time, we create a copy of each node and store it in a dictionary.

Second time, we iterate through the linked list again 
and set the next and random pointers of each copy.

Time: O(n)
Space: O(n)
"""