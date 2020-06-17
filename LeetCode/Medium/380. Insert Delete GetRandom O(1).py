import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dict = {}
        self.realSet = set()
        self.removeItem = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict:
            self.arr.append(val)
            self.dict[val] = len(self.arr)-1

        if val in self.removeItem:
            self.removeItem.remove(val)
        
        if val not in self.realSet:
            self.realSet.add(val)
            return True
        return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            self.removeItem.add(val)
        if val in self.realSet:
            self.realSet.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if len(self.removeItem):
            for v in self.removeItem:
                self.arr[self.dict[v]] = self.arr[-1]
                self.dict[self.arr[-1]] = self.dict[v]
                del self.dict[v]
                del self.arr[-1]

            self.removeItem.clear()

        return self.arr[random.randint(0,len(self.arr)-1)]
        
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_2 = obj.insert(3)
param_2 = obj.remove(3)
param_2 = obj.remove(0)
param_2 = obj.insert(3)
param_2 = obj.getRandom()
