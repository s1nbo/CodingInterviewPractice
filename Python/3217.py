# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p2 = dummy
        p1 = head
        nums = set(nums)

        while p1 != None:
            while p1.val in nums:
                p2.next = p1.next
                p1 = p1.next
                if p1 == None: return dummy.next
            
            p1 = p1.next
            p2 = p2.next
            
        return dummy.next

# Topic: Linked List
# Time Complexity: O(n)
# Space Complexity: O(n)