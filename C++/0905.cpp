#include <vector>
#include <algorithm>
#include <iostream>


class Solution {
public:
    std::vector<int> sortArrayByParity(std::vector<int>& nums) {
        int left = 0, right = nums.size()-1;
        while(left < right){
            while(left < right && nums[left]%2 == 0 ){
                left++;
            }
            while (left < right && nums[right]%2 == 1){
                right--;
            }

            std::swap(nums[left],nums[right]);
        }
        return nums;
    }
};
// Time Complexity: O(n)
// Space Complexity: O(1)
int main(){
    std::vector<int>nums = {3,1,2,4};
    Solution s;
    std::vector<int> res = s.sortArrayByParity(nums);
    return 0;
}