from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        ans = [[-1]*n for _ in range(m)]

        left, right = 0, n-1
        top, bottom = 0, m-1

        while head:
            for i in range(left, right+1):
                if not head: break
                ans[top][i] = head.val
                head = head.next
                
            top += 1
            
            for i in range(top, bottom+1):
                if not head: break
                ans[i][right] = head.val
                head = head.next
                
            right -= 1
            
            for i in range(right, left-1, -1):
                if not head: break
                ans[bottom][i] = head.val
                head = head.next
                
            bottom -= 1
            
            for i in range(bottom, top-1, -1):
                if not head: break
                ans[i][left] = head.val
                head = head.next
                
            left += 1
        
        return ans
    
# Topic: Linked List, Array
# Time complexity: O(m*n)
# Space complexity: O(m*n)