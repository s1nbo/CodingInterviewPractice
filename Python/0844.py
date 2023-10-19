import re
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        while '#' in s:
            s = re.sub('[a-z]#', '', s)
            s = re.sub('^#', '', s)
        while '#' in t:
            t = re.sub('[a-z]#', '', t)
            t = re.sub('^#', '', t)

        return s == t
