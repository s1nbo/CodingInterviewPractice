class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        routes = {start : [] for start, end in tickets}
        tickets.sort()
        for start, end in tickets:
            routes[start].append(end)

        ans = ["JFK"]

        def dfs(current):
            if len(ans) == len(tickets)+1:
                return True
            elif current not in routes:
                return False
        
            temp = list(routes[current])
            for i, j in enumerate(temp):
                routes[current].pop(i)
                ans.append(j)
                if dfs(j): 
                    return True
                routes[current].insert(i, j)
                ans.pop()
            return False

        dfs("JFK")
        return ans

        
"""
Input: list of list of strings
Output: list of strings

We create a dictionary of start and end points
The key is the start point and the value are the end points
By sorting the tickets, we can add the end points in order

Since JFK is the starting point, we add it to the ans
Then we do a dfs to find the path
We pop the end point from the start point and add it to the ans
If this works in every case, we return True
If not, we insert the end point back to the start point and pop it from the ans

Time complexity: O(n^2)
Space complexity: O(n)
"""