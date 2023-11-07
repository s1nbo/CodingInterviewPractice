class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        time_needed = [dist[cur]/speed[cur] for cur in range(len(dist))]
        time_needed.sort()
        print(time_needed)

        for idx, val in enumerate(time_needed):
            if val <= idx:
                return idx
        
        return len(time_needed)
                
        