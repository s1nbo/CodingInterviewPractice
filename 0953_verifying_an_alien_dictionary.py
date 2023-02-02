class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        letter_order = {}
        for i in range(len(order)):
            letter_order[order[i]] = i
        
        for i in range(len(words)-1):
            max_length = max(len(words[i]), len(words[i+1]))
            
            for j in range(max_length):
                
                current_1 = letter_order[words[i][j]] if j < len(words[i]) else -1
                current_2 = letter_order[words[i+1][j]] if j < len(words[i+1]) else -1
                
                if current_1 == current_2:
                    pass
                elif current_1 < current_2:
                    break
                else:
                    return False

        return True


"""
Input: Two lists of strings
Output: Boolean

We create a dictionary that maps each letter to its index in the order string.

We iterate through the words list and compare each word to the next word.
We find the max length of the two words.

We iterate through the max length.
We get the current letter of the first word and the current letter of the second word.
And map them to their index in the order string.

If the current letter of the first word is the same as the current letter of the second word, we pass.
If the current letter of the first word is less than the current letter of the second word, we break.
If the current letter of the first word is greater than the current letter of the second word, we return False.

Finally, we return True.

Time Complexity: O(n) more specifically O(n*m) where n is the number of words and m is the length of the longest word
Space Complexity: O(n) more specifically O(n*m) where n is the number of words and m is the length of the longest word
"""