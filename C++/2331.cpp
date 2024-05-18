// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
 
class Solution {
public:
    bool dfs(TreeNode* root) {
        if (root->val == 0 || root->val == 1) return root->val == 1;
        else if (root->val == 2) return dfs(root->left) || dfs(root->right);
        else return dfs(root->left) && dfs(root->right);
    }
    bool evaluateTree(TreeNode* root){ return dfs(root); }
};