class Solution:
    def sortVowels(self, s: str) -> str:
        vow = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        s = list(s)
        vow_in_s = []
        for i in range(len(s)):
            if s[i] in vow:
                vow_in_s.append(s[i])
                s[i] = '_'

        vow_in_s.sort()

        counter = 0
        for i in range(len(s)):
            if s[i] == '_':
                s[i] = vow_in_s[counter]
                counter += 1
        
        return "".join(s)

# Time complexity: O(n)
# Space complexity: O(n)