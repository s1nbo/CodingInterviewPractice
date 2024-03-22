struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* rev = nullptr;
        ListNode* fast = head;
        ListNode* slow = head;
        
        while(fast && fast->next ){
            fast = fast->next->next;
            ListNode* temp1 = rev;
            ListNode* temp2 = slow->next;
            rev = slow;
            rev->next = temp1;
            slow = temp2;

       }

        if(fast){
            slow = slow->next;
        }
        while(slow and rev->val == slow->val){
            rev = rev->next;
            slow = slow->next;
        }

        return !rev;
    }
};

// Topic: Linked List
// Time Complexity: O(n)
// Space Complexity: O(1)

