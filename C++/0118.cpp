#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > generate(int numRows) {
        vector<vector<int> > res;
        if(numRows == 0) return res;
        vector<int> temp;
        temp.push_back(1);
        res.push_back(temp);

        for(int i = 1; i < numRows; i++){
            vector<int> temp;
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
    vector<vector<int> > res = s.generate(5);
    for(int i = 0; i < res.size(); i++)
    {
        for(int j = 0; j < res[i].size(); j++)
            cout << res[i][j] << " ";
        cout << endl;
    }
    return 0;
}