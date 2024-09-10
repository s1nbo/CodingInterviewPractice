from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def GCD(a, b):
            while b != 0: 
                a, b = b, a % b
            return a

        if head.next == None:
            return head
        prev = head
        cur = head.next

        while cur:
            node_value = GCD(prev.val, cur.val)
            gcd_node = ListNode(val=node_value, next=cur)
            prev.next = gcd_node
            
            cur = cur.next
            prev = prev.next.next
        
        return head

# Topic: Linked List  
# Time Complexity: O(n)
# Space Complexity: O(1)