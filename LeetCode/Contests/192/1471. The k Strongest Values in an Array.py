from typing import List
from operator import itemgetter

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr)-1)//2]
        arr = [(abs(n-median), n) for n in arr]
        return [n[1] for n in sorted(arr, key=itemgetter(0,1), reverse=True)][:k]

a = Solution()
print(a.getStrongest([1,2,3,4,5],2))