#include <math.h>

class Solution {
public:
    int findClosest(int x, int y, int z) {
        int d1 = abs(x-z);
        int d2 = abs(y-z);
        if (d1 < d2) return 1;
        else if (d1 > d2) return 2;
        return 0;
    }
};