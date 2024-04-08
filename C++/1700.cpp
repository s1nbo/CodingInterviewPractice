#include <vector>

class Solution {
public:
    int countStudents(std::vector<int>& students, std::vector<int>& sandwiches) {
        int ans = students.size();
        std::vector<int> count = {0, 0};
        for(int student : students) {
            count[student]++;
        }
        for(int sandwich : sandwiches) {
            if (count[sandwich] == 0) break;
            count[sandwich]--;
            ans--;
        }
        return ans;
    }
};

// Topic: Array
// Time Complexity: O(n)
// Space Complexity: O(1)