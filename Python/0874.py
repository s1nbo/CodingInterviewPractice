from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        cur_direction = 0
        direction = [[0,1], [1,0], [0,-1], [-1,0]]
        pos = [0, 0]
        ans = 0
        obstacles_dict = set(map(tuple, obstacles))

        for command in commands:
            if command == -1:
                cur_direction = (cur_direction+1) % 4
            elif command == -2:
                cur_direction = (cur_direction-1) % 4
            else:

                for i in range(command):
                    if (pos[0]+direction[cur_direction][0], pos[1]+direction[cur_direction][1]) not in obstacles_dict:
                        pos[0] += direction[cur_direction][0]
                        pos[1] += direction[cur_direction][1]
                    else:
                        break
                        
                ans = max(ans, pos[0]**2 + pos[1]**2)

        return ans