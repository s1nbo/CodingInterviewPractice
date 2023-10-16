class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        prev = 1
        ans = [1]
        
        for i in range(1, rowIndex+1):
            cur = prev * (rowIndex-i+1) // i
            ans.append(cur)
            prev = cur

        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)
