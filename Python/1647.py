import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        used = [] # can also be used = set()
        freq = collections.Counter(s)
        # freq = {}
        # for i in s:
        #     if i not in freq:
        #         freq[i] = 1
        #     else:
        #         freq[i] += 1
        
        for _, j in freq.items():
            while j in used and j > 0:
                j -= 1
                ans += 1
            used.add(j)
        
        return ans
    
"""
Input: String
Output: Integer

First we need to find the frequency of each character in the string
This can be done with collections.Counter() (Dictionary)

Then we need to find the minimum number of deletions to make the frequency of each character unique
We can do this by keeping track of the used frequencies in a set
If the frequency is already in the set, we need to decrement the frequency until it is not in the set
We also need to keep track of the number of deletions we make

Return the number of deletions

Time Complexity: O(n)
Space Complexity: O(n)
"""