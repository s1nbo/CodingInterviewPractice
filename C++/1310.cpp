#include <vector>


class Solution {
public:
    std::vector<int> xorQueries(std::vector<int>& arr, std::vector<std::vector<int>>& queries) {
        std::vector<int> prefix(arr.size());
        std::vector<int> ans(queries.size());
        prefix[0] = arr[0];

        for(int i = 1; i < arr.size(); ++i){
            prefix[i] = prefix[i-1] ^ arr[i];
        }

        for(int i = 0; i < queries.size(); ++i){
            int left = queries[i][0];
            int right = queries[i][1];

            if (left == 0){
                ans[i] = prefix[right];
            } else {
                ans[i] = prefix[right] ^ prefix[left-1];
            }
        }
        
        return ans;
    }
};

// Topic: Bit Manipulation
// Time Complexity: O(n + m)
// Space Complexity: O(n + m)