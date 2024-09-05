from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        m_sum = sum(rolls)
        temp = (n+m)*mean
        n_sum = temp-m_sum
        
        if n_sum > 6*n or n_sum < 1*n:
            return []
        

        n_mean, remainder = divmod(n_sum, n)
        #n_mean = n_sum // n
        #remainder = n_sum % n
        
        ans = [n_mean+1]*remainder + [n_mean]*(n-remainder)
        return ans

# Topic: Math
# Time Complexity: O(m)
# Space Complexity: O(1)
