#include <string>
#include <unordered_map>

class Solution {
public:
    std::string customSortString(std::string order, std::string s) {
        std::string ans = "";
        std::unordered_map<int, int> count;

        for(auto& cur : s){
            count[cur]++;
        }
        for(auto& cur : order){
            if(count.find(cur) != count.end()){
                ans.append(count[cur], cur);
                count.erase(cur);
            }
        }
        for(auto& cur : count){
            ans.append(cur.second, cur.first);
        }
        return ans;
    }
};
