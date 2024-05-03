class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        len_v1 = len(v1)
        len_v2 = len(v2)

        len_min = min(len_v1, len_v2)
        len_max = max(len_v1, len_v2)

        for i in range(len_min):
            v1_int, v2_int = int(v1[i]), int(v2[i])
            if v1_int > v2_int:
                return 1
            elif v1_int < v2_int:
                return -1
        
        for i in range(len_min, len_max):
            if i >= len_v1 and int(v2[i]) != 0:
                return -1
            elif i >= len_v2 and int(v1[i]) != 0:
                return 1

        return 0

# Topic: String
# Time Complexity: O(n)
# Space Complexity: O(n)