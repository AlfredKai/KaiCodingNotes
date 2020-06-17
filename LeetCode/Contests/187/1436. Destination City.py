from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        fromCity = set()
        toCity = set()
        for c in paths:
            fromCity.add(c[0])
            toCity.add(c[1])
        return (toCity - fromCity).pop()

a = Solution()
print(a.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))