# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if head == None:
            return None
        
        slow = head
        fast = head

        while True:
            slow = slow.next
            for _ in range(2):
                fast = fast.next
                if fast == None:
                    return None
            if fast == slow:
                break
        
        slow = head

        while fast != slow:
            fast = fast.next
            slow = slow.next
            
        return slow

"""
Input: Linked List
Output: Node

We initialize two pointers, slow and fast, to the head of the linked list.

We loop through the linked list.
We move slow one node forward.
We move fast two nodes forward.
If fast is None, we return None.
If fast is equal to slow, we break out of the loop.

We set slow to the head of the linked list.

We loop through the linked list.
We move fast one node forward.
We move slow one node forward.

We return slow when it is equal to fast.

Time Complexity: O(n)
Space Complexity: O(1)
"""
        