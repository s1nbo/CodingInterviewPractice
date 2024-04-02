class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ST = {}
        TS = {}

        for i in range(len(s)):
            if s[i] in ST:
                if ST[s[i]] != t[i]:
                    return False
            elif t[i] in TS:
                    return False
            
            ST[s[i]] = t[i]
            TS[t[i]] = s[i]

        return True

# Topic: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)