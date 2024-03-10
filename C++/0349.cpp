#include <vector>
#include <unordered_set>

class Solution {
public:
    std::vector<int> intersection( std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_set<int> set1(nums1.begin(), nums1.end());
        std::unordered_set<int> set2(nums2.begin(), nums2.end());
        std::vector<int> ans;
        
        for(auto cur : set1){
            if (set2.find(cur) != set2.end()){
                ans.push_back(cur);
            } 
        }
        return ans;
    }
};

// Topic: Array
// Time Complexity: O(n)
// Space Complexity: O(n)