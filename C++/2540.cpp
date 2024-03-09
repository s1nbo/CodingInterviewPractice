#include <vector>
class Solution {
public:
    int getCommon(std::vector<int>& nums1, std::vector<int>& nums2) {
        int first{0}, second{0};

        while(first < nums1.size() && second < nums2.size()){
            if (nums1[first] == nums2[second]) return nums1[first];
            nums1[first] > nums2[second] ? second++ : first++;
        }
        return -1;
    }
};

// Topic: Two Pointers
// Time: O(n + m)
// Space: O(1)
