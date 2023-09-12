#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> generate(int numRows) {
        std::vector<std::vector<int>> res;
        if(numRows == 0) return res;
        std::vector<int> temp;
        temp.push_back(1);
        res.push_back(temp);

        for(int i = 1; i < numRows; i++){
            std::vector<int> temp;
            temp.push_back(1);
            for(int j = 1; j < i; j++){
                temp.push_back(res[i-1][j]+res[i-1][j-1]);
            }
            temp.push_back(1);
            res.push_back(temp);
        }
        return res;
    }
};

int main()
{
    Solution s;
    std::vector<std::vector<int>> res = s.generate(5);
    for(int i = 0; i < res.size(); i++)
    {
        for(int j = 0; j < res[i].size(); j++)
            std::cout << res[i][j] << " ";
        std::cout << std::endl;
    }
    return 0;
}