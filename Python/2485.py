import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        x = math.sqrt((n*(n+1)/2))
        return int(x) if x == int(x) else -1