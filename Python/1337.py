import heapq

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        min_heap = []
        for idx, row in enumerate(mat):
            heapq.heappush(min_heap, (sum(row), idx))
        return[heapq.heappop(min_heap)[1] for _ in range(k)]

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
