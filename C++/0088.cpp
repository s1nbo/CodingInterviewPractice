#include <vector>

class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        while( n > 0 ) {
            if (m > 0 && nums1[m-1] >= nums2[n-1] ){
                nums1[m+n-1] = nums1[m-1];
                m--;
            } else {
                nums1[m+n-1] = nums2[n-1];
                n--;
            }
        }
    }
};

// Time Complexity: O(n)
// Space Complexity: O(1)