class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []

        p_count = {}
        s_count = {}
        answer = []
        left_pointer = 0
        right_pointer = len(p)
        
        for i in range(len(p)):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        while True:
            if p_count == s_count:
                answer.append(left_pointer)

            if right_pointer == len(s):
                return answer
            
            if s_count[s[left_pointer]] > 1:
                s_count[s[left_pointer]] -= 1
            else: 
                s_count.pop(s[left_pointer])
            left_pointer += 1

            s_count[s[right_pointer]] = s_count.get(s[right_pointer ], 0) + 1
            right_pointer += 1


"""
Input: Two strings
Output: List of integers

First we check if the length of p is greater than the length of s. 
If it is, we know that p cannot be an anagram of s, so we return an empty list.

Next, we create two dictionaries.
One dictionary will hold the amount of each character in p.
The other dictionary will hold the amount of each character in s.

We do this by iterating through p and adding each character to the dictionary with a value of 1 if it is not already in the dictionary.
If it is already in the dictionary, we increment the value by 1.
We do the same thing for s except we only iterate through the first len(p) characters.

Next, we create a list that will hold the indices of the start of each anagram. (answer)
We create two pointers, left_pointer and right_pointer.
We set left_pointer to 0 and right_pointer to len(p).

Next, we create a while loop that will run until right_pointer is equal to the length of s.
In the while loop, we check if the two dictionaries are equal.
If they are, we append the left_pointer to the answer list, because that is the start of an anagram.

Next, we check if right_pointer is equal to the length of s.
If it is, we return the answer list.

Next, we remove the character at the left_pointer from the dictionary.
If the value of the character is greater than 1, we decrement the value by 1.
If the value of the character is 1, we remove the character from the dictionary.
After we remove the character, we increment the left_pointer by 1.

Next, we add the character at the right_pointer to the dictionary.
If the character is already in the dictionary, we increment the value by 1.
If the character is not in the dictionary, we add it to the dictionary with a value of 1.
After we add the character, we increment the right_pointer by 1.

Time Complexity: O(n)
Space Complexity: O(n)
"""