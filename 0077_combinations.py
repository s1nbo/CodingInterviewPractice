class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        
        def backtracking(start, current):
            if len(current) == k:
                ans.append(current.copy())
                return
            
            for i in range(start, n+1):
                current.append(i)
                backtracking(i+1, current)
                current.pop()
            
        backtracking(1, [])
        return ans


"""
Input: Two integers
Output: List of lists of integers

We use backtracking to generate all possible combinations of k numbers out of 1 ... n.

If the lenght of the current combination is equal to k, we add it to the answer.

Otherwise, we iterate over the numbers from start to n+1, and add them to the current combination.
Then, we call the backtracking function again, with the start index increased by 1.
After that, we remove the last element from the current combination, and repeat the process.

Time complexity: O(n^k)
Space complexity: O(n^k)
"""