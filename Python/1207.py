from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = Counter(arr)
        
        """
        unique = set()
        for i in count.values():
            if i in unique:
                return False
            unique.add(i)
        return True
        """
        return len(count) == len(set(count.values()))

# Topic: hash table
# Time complexity: O(n)
# Space complexity: O(n)
