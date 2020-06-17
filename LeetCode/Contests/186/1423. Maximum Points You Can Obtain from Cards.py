from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        accuLeft = [0] * k
        accuLeft[0] = cardPoints[0]
        for i in range(1,k):
            accuLeft[i] = accuLeft[i-1] + cardPoints[i]
        accuRight = [0] * k
        accuRight[k-1] = cardPoints[-1]
        cpi = len(cardPoints) - 2
        for i in reversed(range(k-1)):
            accuRight[i] = accuRight[i + 1] + cardPoints[cpi]
            cpi -= 1
        r = max(accuLeft[-1], accuRight[0])
        for i in range(k-1):
            sum = accuLeft[i] + accuRight[i+1]
            if sum > r:
                r = sum
        return r

a = Solution()
print(a.maxScore([1,2,3,4,5,6,1], 3))