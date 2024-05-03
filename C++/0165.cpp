#include <vector>
#include <string>

class Solution {
public:
    int compareVersion(std::string version1, std::string version2) {
        std::vector<int> v1, v2;
        std::string temp;
    
    // Split version1 into vector
    for (char c : version1) {
        if (c == '.') {
            v1.push_back(std::stoi(temp));
            temp.clear();
        } else {
            temp += c;
        }
    }
    v1.push_back(std::stoi(temp));
    
    // Split version2 into vector
    temp.clear();
    for (char c : version2) {
        if (c == '.') {
            v2.push_back(std::stoi(temp));
            temp.clear();
        } else {
            temp += c;
        }
    }
    v2.push_back(std::stoi(temp));
    
    // Compare versions
    int len_v1 = v1.size();
    int len_v2 = v2.size();
    int len_min = std::min(len_v1, len_v2);
    int len_max = std::max(len_v1, len_v2);
    
    for (int i = 0; i < len_min; i++) {
        if (v1[i] > v2[i]) {
            return 1;
        } else if (v1[i] < v2[i]) {
            return -1;
        }
    }

    for (int i = len_min; i < len_max; i++) {
        if (i >= len_v1 && v2[i] != 0) {
            return -1;
        } else if (i >= len_v2 && v1[i] != 0) {
            return 1;
        }
    }
    return 0;
    }
};

// Topic: String
// Time Complexity: O(n)
// Space Complexity: O(n)
