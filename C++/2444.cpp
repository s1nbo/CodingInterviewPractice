#include <algorithm>
#include <vector>
class Solution {
public:
    long long countSubarrays(std::vector<int>& nums, int minK, int maxK) {
        long long ans = 0;
        int cur_min = -1, cur_max = -1, invalid = -1;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == minK){
                cur_min = i;
            }
            if(nums[i] == maxK){
                cur_max = i;
            }
            if(nums[i] < minK || nums[i] > maxK){
                invalid = i;
            }
            ans += std::max(0, (std::min(cur_min, cur_max)-invalid));
        }
        return ans;
    }
};