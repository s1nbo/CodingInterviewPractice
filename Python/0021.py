# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1


        if list1.val <= list2.val:
            head = list1
            list1 = list1.next

        else:
            head = list2
            list2 = list2.next

        current = head


        while list1 != None or list2 != None:
            if list1 == None:
                current.next = list2
                break
            elif list2 == None:
                current.next = list1
                break
            elif list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next 


        return head


"""
Input: two linked lists
Output: a linked list

Check if one of the lists is empty.
If one of the lists is empty, return the other list.

Create a head node and a current node.
If the value of list1 is smaller than the value of list2, set the head node to list1 and set list1 to list1.next. (vice versa)

Set the current node to the head node.

While list1 and list2 are not empty:
    If list1 is empty, set the current node to list2 and break. (vice versa)

    If the value of list1 is smaller than the value of list2, set the current node to list1 and set list1 to list1.next.
    Append one node from list1 to the current chain of nodes (answer).
    (vice versa)

    Set the current node to the next node.

Return the head node.

Time Complexity: O(n)
Space Complexity: O(1)
"""