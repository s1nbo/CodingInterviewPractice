# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        curr = ListNode()
        head = curr
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10
        
        return head.next


"""
Input: two linked lists
Output: a linked list that is the sum of the two input linked lists

Create a new linked list to store the sum of the two input linked lists.
Create a carry variable to store the carry over value.

Iterate through the two linked lists and add the values together.
If the sum is greater than 10, then we need to carry over the 1 to the next value and subtract 10 from the current value.

Time Complexity: O(n)
Space Complexity: O(n)
"""   