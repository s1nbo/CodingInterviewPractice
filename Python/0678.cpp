class Solution {
public:
    bool checkValidString(string s) {
        int open_count = 0, close_count = 0;

        for(int i = 0; i < s.length(); i++){
            if (s[i] == '(' || s[i] == '*') open_count++;
            else open_count--;
            if (s[s.length() - i - 1] == ')' || s[s.length() - i - 1] == '*') close_count++;
            else close_count--;
            if (open_count < 0 || close_count < 0) return false;
        }
        return true;
    }
};

// Topic: String, Stack (Not used)
// Time Complexity: O(n)
// Space Complexity: O(1)