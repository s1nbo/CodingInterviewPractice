class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ 2**num.bit_length()-1
    # This works because XOR with 1 flips the bit, and the second term creates a mask with all 1s of the same length as num.


# Topics: Bit Manipulation
# Time Complexity: O(1)
# Space Complexity: O(1)
        