class Solution:
    def hasCycle(self, head) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        
        return False


"""
Input: Linked List head
Output: Boolean

We use the fast and slow pointer method to detect a cycle in a linked list.
We have two pointers, fast and slow. Fast moves two nodes at a time and slow moves one node at a time.
If there is a cycle, the fast and slow pointer will eventually meet.

Time Complexity: O(n)
Space Complexity: O(1)
"""