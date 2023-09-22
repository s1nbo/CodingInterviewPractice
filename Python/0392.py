class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        pointer = 0
        for char in t:
            if s[pointer] == char:
                pointer += 1
                if pointer == len(s):
                    return True

        return False
            