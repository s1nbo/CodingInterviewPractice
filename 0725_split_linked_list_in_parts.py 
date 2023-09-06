# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: [ListNode], k: int) -> [[ListNode]]:
        # 1
        amount = 0
        cur = head
        while cur:
            amount += 1
            cur = cur.next
        # 2
        length, rest = amount // k, amount % k
        # 3
        answer = []
        cur = head
        for i in range(k):
            answer.append(cur)

            for j in range(length-1 + (1 if rest > 0 else 0)):
                if not cur:
                    break
                cur = cur.next
            
            if cur:
                cur.next, cur = None, cur.next # Python magic
            rest -= 1
        # 4
        return answer

"""
Input: Linked List head
Output: List of Linked Lists

1. Find the length of the linked list

2. Find the length of each part (split equally into k parts)
Find the remainder of the length of the linked list divided by k (the first n parts will have an extra node)

3. Split the linked list into k parts
Each part will have a inital node appended
Then we iterate with j from 0 to length-1 (+1 for the first n parts), length-1 because by default we have 1 node in each part.
if cur is None, then we break
After iterating, we set cur.next to None, and cur = cur.next (python magic) to split the linked list and move on to the next part
the rest will be decremented by 1 each time, so that the first n parts will have an extra node

4. Return the answer

Time Complexity: O(n + k) where n is the number of nodes in the linked list
Space Complexity: O(k) where k is the number of parts we split the linked list into
"""
        