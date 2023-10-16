class Solution {
public:
    vector<int> getRow(int rowIndex) {
        int prev = 1;
        vector<int> ans = {1};

        for(int i = 1; i <= rowIndex; i++){
            long cur = prev * (rowIndex - i + 1) / i;
            ans.push_back(cur);
            prev = cur;
        }
        return ans;
    }
};

// Time Complexity: O(n)
// Space Complexity: O(n)