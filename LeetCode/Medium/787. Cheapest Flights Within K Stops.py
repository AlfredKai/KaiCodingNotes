from typing import List
from collections import defaultdict, deque
from heapq import heappush, heappop


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for f in flights:
            graph[f[0]].append([f[1], f[2]])

        heap = [[0, -1, src]]

        while heap:
            cost, steps, node = heappop(heap)

            if steps > K:
                continue

            if node == dst:
                return cost

            for v, w in graph[node]:
                heappush(heap, [cost+w, steps+1, v])

        return -1

class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for f in flights:
            graph[f[0]].append([f[1], f[2]])
        que = deque()
        que.append(src)
        while que:
            

a = Solution()
print(a.findCheapestPrice(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1))
