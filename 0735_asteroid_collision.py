class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack and stack[-1] == abs(asteroid):
                    stack.pop()
                
        return stack


"""
Input: list of integers
Output: list of integers

We create a stack to keep track of the asteroids that are still in the sky.

We iterate through the asteroids. If the stack is empty or the asteroid is positive, we add it to the stack.
If the asteroid is negative, we check if the stack is empty or the top of the stack is positive and less than the absolute value of the current asteroid.
If it is, we pop the top of the stack. We continue to do this until the stack is empty or 
the top of the stack is negative or 
the top of the stack is greater than the absolute value of the current asteroid.

If the stack is empty or the top of the stack is negative, we add the current asteroid to the stack.
If the top of the stack is equal to the absolute value of the current asteroid, we pop the top of the stack.
If the postive asteroid is greater than the absolute value of the current asteroid, we do nothing.

We return the stack.

Time complexity: O(n)
Space complexity: O(n)
"""
            