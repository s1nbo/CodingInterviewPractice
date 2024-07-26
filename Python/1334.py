from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        distance = [[float('inf')] * n for _ in range(n)]

        # Fill distance matrix
        for i in range(n):
            distance[i][i] = 0
    
        for start, end, weight in edges:
            distance[start][end] = weight
            distance[end][start] = weight

        
        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min( distance[i][j], ( distance[i][k] + distance[k][j] ) )

        # Best City
        city_ans = -1
        amount_ans = float('inf')

        for i in range(n):
            reachable_cities = 0
            for j in range(n):
                reachable_cities += (distance[i][j] <= distanceThreshold)

            if reachable_cities <= amount_ans:
                amount_ans = reachable_cities
                city_ans = i

        return city_ans