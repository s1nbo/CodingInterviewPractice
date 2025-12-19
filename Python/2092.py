from collections import defaultdict
from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        ans = {0, firstPerson}

        meetings_dict = {}
        
        for x, y, time in meetings:
            if time not in meetings_dict:
                meetings_dict[time] = defaultdict(list)

            meetings_dict[time][x].append(y)
            meetings_dict[time][y].append(x)

        def dfs(start, adj):
            if start in visit:
                return
            visit.add(start)
            ans.add(start)
            for neighbor in adj[start]:
                dfs(neighbor, adj)

        for time in sorted(list(meetings_dict.keys())):
            visit = set()
            for start in meetings_dict[time]:
                if start in ans:
                    dfs(start, meetings_dict[time])


        return list(ans)


# Time Complexity: O(M log M + M + N) where M is the number of meetings and N is the number of people
# simplified to O(M log M + N)
# Space Complexity: O(M + N)