#include <vector>
#include <string>
#include <unordered_set>
#include <queue>

class Solution {
public:
    int openLock(std::vector<std::string>& deadends, std::string target) {
        std::unordered_set<std::string> set_deadends(deadends.begin(), deadends.end());

        if(set_deadends.find("0000") != set_deadends.end()) return -1;
        
        std::unordered_set<std::string> visited;
        visited.insert("0000");

        std::queue<std::pair<std::string, int>> q;
        q.push({"0000",0});

        while(!q.empty()){
            std::string cur = q.front().first;
            int moves = q.front().second;
            q.pop();

            if(cur == target) return moves;

            for(int i = 0; i < 4; i++){
                for(int change : {-1, 1}) {
                    int new_digit = (cur[i] - '0' + change + 10) % 10;
                    std::string temp = cur.substr(0, i) + std::to_string(new_digit) + cur.substr(i + 1);

                    if(visited.find(temp) == visited.end() && set_deadends.find(temp) == set_deadends.end()){
                        visited.insert(temp);
                        q.push({temp, moves+1});
                    }
                }
            }
        }
        return -1;
    }
};

// Topic: Breadth First Search
// Time Complexity: O(1)
// Space Complexity: O(1)