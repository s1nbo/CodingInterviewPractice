#include <vector>
class Solution {
public:
    std::vector<int> searchRange(std::vector<int>& nums, int target) {
        
        return {binarySearch(nums, target, true), binarySearch(nums, target, false)};
    }
    
    int binarySearch(std::vector<int>& nums, int target, bool left_bias){
        
        int left = 0, right = nums.size()-1, ans = -1;
        
        while(left <= right){
            int mid = (left + right) / 2;
            
            if (nums[mid] > target) right = mid-1;
            else if (nums[mid] < target) left = mid+1;
            else {
                ans = mid;
                if(left_bias) right=mid-1;
                else left = mid+1;
            }
        }

        return ans;
    }
};
// Time Complexity: O(logn)
// Space Complexity: O(1)