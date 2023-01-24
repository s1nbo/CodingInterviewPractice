class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.minstack): 
            self.minstack.append(min(val, self.minstack[-1]))  
        else: 
            self.minstack.append(val)
            


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


"""
Input: None
Output: None

We initialize two stacks. One for the stack and one for the minstack.

We define a push method that takes in a value.
We append the value to the stack.

If the minstack is not empty, we append the minimum of the value and the last value of the minstack to the minstack.
If the minstack is empty, we append the value to the minstack.

We define a pop method that takes in no value.
We pop the last value of the stack.

We define a top method that takes in no value.
We return the last value of the stack.

We define a getMin method that takes in no value.
We return the last value of the minstack.

Time Complexity: O(1)
Space Complexity: O(n)
"""