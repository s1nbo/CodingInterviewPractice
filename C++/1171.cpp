#include <unordered_map>
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode* dummy = new ListNode(0,head);
        int prefix_sum = 0;
        std::unordered_map<int, ListNode*> prefix_sums;
        ListNode* current = dummy;

        while(current){
            prefix_sum += current->val;
            prefix_sums[prefix_sum] = current;
            current = current->next;
        }

        prefix_sum = 0;
        current = dummy;

        while(current){
            prefix_sum += current->val;
            current->next = prefix_sums[prefix_sum]->next;
            current = current->next;
        }
        return dummy->next;    
    }
};

// Topic: Linked List, Hash Table
// Time Complexity: O(n)
// Space Complexity: O(n)