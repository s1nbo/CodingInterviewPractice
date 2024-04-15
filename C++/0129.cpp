
#include <vector>
#include <string>
#include <algorithm>

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
    int sumNumbers(TreeNode* root) {
        return helper(root, {});
    }
private:
    int helper(TreeNode* node, std::vector<int> path) {
        if (!node) return 0;
        path.push_back(node->val);
        int ans = 0;
        if (!node->left && !node->right) {
            std::string num = "";
            for (int digit : path) {
                num += std::to_string(digit);
            }
            return stoi(num);
        }
        ans += helper(node->left, path);
        ans += helper(node->right, path);
        return ans;
    }
};