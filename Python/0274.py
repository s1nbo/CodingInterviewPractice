class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        n = len(citations)
        for i, v in enumerate(citations):
            if n - i <= v:
                return n - i

        return 0

# Topic: Array
# Time Complexity: O(nlogn)
# Space Complexity: O(1)