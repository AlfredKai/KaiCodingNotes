import typing


from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        r = []
        def DFS(v, path:list, visited:set):
            if v == len(graph)-1:
                p = path.copy()
                p.append(v)
                r.append(p)
                return
            p = path.copy()
            p.append(v)
            visit = visited.copy()
            visit.add(v)
            for conn_v in graph[v]:
                if conn_v not in visited:
                    DFS(conn_v, p, visit)
        DFS(0, [], set())
        return r

a = Solution()
a.allPathsSourceTarget([[1,2],[3],[3],[]])