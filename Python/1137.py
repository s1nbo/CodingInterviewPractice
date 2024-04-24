class Solution:
    def tribonacci(self, n: int) -> int:
        # Base case
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n+1):
            a, b, c = b, c, a+b+c
        
        return c
        
""""
Input: integer
Output: integer



sequence = [0,1,1]
        
        for i in range(3, n+1):
            sequence.append(sequence[i-1]+sequence[i-2]+sequence[i-3])
        
        return sequence[n]

We use a list to store the first 3 numbers of the sequence.
We use a for loop to add the next number to the list.
We return the nth number of the sequence.

Time Complexity: O(n)
Space Complexity: O(n)
"""