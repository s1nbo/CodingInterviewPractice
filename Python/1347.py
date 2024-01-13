import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        ans = 0
        for i in s_count.keys():
            ans += max(s_count[i]-t_count[i], 0)
        
        return ans

        