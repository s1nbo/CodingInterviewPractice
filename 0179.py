from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        ans = (list(map(str, nums)))
        ans.sort(key=lambda x: x*10, reverse=True)

        if ans[0] == '0':
            return '0'

        return ''.join(ans)
