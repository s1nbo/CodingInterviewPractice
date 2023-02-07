class Solution:
    def totalFruit(self, fruits) -> int:
        left = 0
        best = 1
        current = 0
        distinct_fruits = [fruits[0]]
        
        if len(fruits) < 3:
            return len(fruits)
        
        for right in range(len(fruits)):
            if fruits[right] in basket:
                current += 1
            elif len(basket) == 1:
                basket.append(fruits[right])
                current += 1
            else:
                best = max(current, best)
                basket = [fruits[right]]
                current = 0
                for backtrack in range(right, left, -1):
                    if fruits[backtrack] in basket:
                        current += 1
                    elif len(basket) == 1:
                        basket.append(fruits[backtrack])
                        current += 1
                    else:
                        break

        return max(current, best)


"""
Input: list of integers
Output: integer

We create a left pointer, best, current, and basket.

If the length of the list is less than 3, we return the length of the list.

We iterate through the list.
If the current fruit is in the basket, we increment current.
If their is only one fruit in the basket, we add the current fruit to the basket and increment current. 
If we have two fruits in the basket and encounter a third, we update best.
We reset the basket to the current fruit.
We reset current to 0.
We iterate through the list backwards.
If the current fruit is in the basket, we increment current.
If their is only one fruit in the basket, we add the current fruit to the basket and increment current.
If we have two fruits in the basket and encounter a third, we break.

We return the maximum of current and best.

Time Complexity: O(n)
Space Complexity: O(n)
"""