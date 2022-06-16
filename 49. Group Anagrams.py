class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {} # counter array that counts chars in strs -> strings in strs
        
        for string in strs:
            counter = [0] * 26 # For every lowercase letter one Index
            
            for letter in string:
                counter[ord(letter)-ord("a")] += 1 # ord returns unicode code and a is index 0
            
            if tuple(counter) in result:
                result[tuple(counter)].append(string)
            else:
                result[tuple(counter)] = [string]
            
        return result.values()


"""
Input: array of strings
Output: 2D array of strings

First we initialize a result hash table. We store a counter array that counts chars in strs -> strings in strs.
So every string in strs with the same letters will be in the same bucket.

We iterate through strs and through each string in strs to count the letters.
Then we add the string to the result hash table.
We return the result hash table values (the strings in strs reodered by their letters).

Time Complexity: O(n)
Space Complexity: O(n)
"""