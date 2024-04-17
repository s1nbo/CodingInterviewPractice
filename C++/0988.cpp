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
    std::string smallestFromLeaf(TreeNode* root) {
        std::string ans = "{";
        std::vector<char> path;
        dfs(root, path, ans);
        return ans;
    }

private:
    void dfs(TreeNode* node, std::vector<char>& path, std::string& ans) {
        if (!node) {
            return;
        }

        path.push_back(static_cast<char>(node->val + 'a'));

        if (!node->left && !node->right) {
            std::string cur(path.rbegin(), path.rend());
            ans = std::min(ans, cur);
        }

        dfs(node->left, path, ans);
        dfs(node->right, path, ans);

        path.pop_back();
    }
};

// Topic: Tree, Dfs
// Time Complexity: O(n)
// Space Complexity: O(h) height of the tree