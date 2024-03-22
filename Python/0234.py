# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        rev = None
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            temp1 = rev
            temp2 = slow.next if slow else None

            rev = slow
            if rev:
                rev.next = temp1
            slow = temp2

        if fast: # for odd lists
            slow = slow.next if slow else None

        while rev and slow and rev.val == slow.val:
            rev = rev.next
            slow = slow.next if slow else None


        return not rev
    
# Topic: Linked List
# Time Complexity: O(n)
# Space Complexity: O(1)