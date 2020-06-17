from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        maxH = max(horizontalCuts[0] - 0, h - horizontalCuts[-1])
        for i in range(len(horizontalCuts)):
            maxH = max(maxH, horizontalCuts[i] - horizontalCuts[i-1])
        verticalCuts.sort()
        maxV = max(verticalCuts[0] - 0, w - verticalCuts[-1])
        for i in range(len(verticalCuts)):
            maxV = max(maxV, verticalCuts[i] - verticalCuts[i-1])
        modV = 1000000000
        r = maxV * maxH
        if r > modV:
            r = r % (modV + 7)
        return r
