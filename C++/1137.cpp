class Solution {
public:
    int tribonacci(int n) {
        if(n == 0) return 0;
        if(n == 1 || n == 2) return 1;

        int a = 0, b = 1, c = 1, temp;
        for(int i = 3; i <= n; i++){
            temp = c;
            c += a+b;
            a = b;
            b = temp;
        }
        return c;
    }
};

// Topic: Dynamic Programming, Recursion
// Time Complexity: O(n)
// Space Complexity: O(1)