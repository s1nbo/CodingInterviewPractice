from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val = 0, next = head)
        prefix_sum = 0
        prefix_sums = {}
        current = dummy

        while current:
            prefix_sum += current.val
            prefix_sums[prefix_sum] = current
            current = current.next

        prefix_sum = 0
        current = dummy

        while current:
            prefix_sum += current.val
            current.next = prefix_sums[prefix_sum].next
            current = current.next
        
        return dummy.next

# Topic: Linked List, Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)