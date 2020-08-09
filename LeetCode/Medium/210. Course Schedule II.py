from types import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for edge in prerequisites:
            indegree[edge[0]] += 1
            graph[edge[1]].append(edge[0])
        zero_indegree = deque()
        for v in range(numCourses):
            if indegree[v] == 0:
                zero_indegree.append(v)
        r = []
        while zero_indegree:
            v = zero_indegree.popleft()
            r.append(v)
            for neighbor in graph[v]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    zero_indegree.append(neighbor)
        if len(r) < numCourses:
            return []
        return r