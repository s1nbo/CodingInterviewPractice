#include <vector>
#include <algorithm>
class Solution {
public:
    long long countSubarrays(std::vector<int>& nums, int k) {
        int target = *std::max_element(nums.begin(), nums.end()), counter = 0, l = 0;
        long long ans = 0;
        for(auto r : nums){
            counter += r == target;
            while(counter == k) counter -= nums[l++] == target; 
            ans += l;  
        }  
        return ans;
    }
};