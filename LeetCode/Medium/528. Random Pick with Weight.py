from typing import List 
from random import randrange
import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.bst = [w[0]]
        for i in range(1, len(w)):
            self.bst.append(w[i] + self.bst[i-1])

    def pickIndex(self) -> int:
        if len(self.bst) == 1:
            return 0
        rn = randrange(1,self.bst[-1]+1)
        return bisect.bisect_left(self.bst, rn)


# Your Solution object will be instantiated and called as such:
# obj = Solution([1])
# obj = Solution([3,14,1,7])
obj = Solution([1,3])
param_1 = obj.pickIndex()
param_1 = obj.pickIndex()
param_1 = obj.pickIndex()
param_1 = obj.pickIndex()
param_1 = obj.pickIndex()