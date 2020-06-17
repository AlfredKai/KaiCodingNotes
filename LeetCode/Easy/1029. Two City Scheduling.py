from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = [[i, c[0] - c[1]] for i, c in enumerate(costs)]
        diff.sort(key=lambda x: x[1])
        r = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                r += costs[diff[i][0]][0]
            else:
                r += costs[diff[i][0]][1]
        return r