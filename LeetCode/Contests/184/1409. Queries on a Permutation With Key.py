from typing import List
from collections import deque

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = deque([i for i in range(1,m+1)])
        r = []
        for i in range(len(queries)):
            r.append(P.index(queries[i]))
            P.remove(queries[i])
            P.appendleft(queries[i])
        return r

a = Solution()
print(a.processQueries([3,1,2,1], 5))