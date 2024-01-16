import random

class RandomizedSet:
    def __init__(self):
        self.set = []
        self.where = {}
        

    def insert(self, val: int) -> bool:
        if val in self.where:
            return False
        self.set.append(val)
        self.where[val] = len(self.set)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.where:
            return False
        
        # We overwrite the value to be removed and remove the value from the dict
        current = self.where[val] 
        self.set[current] = self.set[-1] # overwrite
        self.where[self.set[current]] = current # update index in dict
        
        self.set.pop() 
        del self.where[val] # remove val 
        
        return True
        
        

    def getRandom(self) -> int:
        return random.choice(self.set)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
    
# Topic: Array, Hash Table, Design
# Time Complexity: O(1)
# Space Complexity: O(n)