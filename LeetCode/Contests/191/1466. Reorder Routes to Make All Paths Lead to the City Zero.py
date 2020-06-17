from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        r = [0]
        graph = [[0]*n for i in range(n)]
        for e in connections:
            graph[e[0]][e[1]] = 1
        def DFS(v, visited):
            visited.add(v)
            for i in range(n):
                if i not in visited:
                    if graph[v][i] == 1:
                        r[0] += 1
                    if graph[v][i] == 1 or graph[i][v] == 1:
                        DFS(i, visited)
        DFS(0, set())
        return r[0]

class Solution2:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        r = [0]
        outEdges = {}
        inEdges = {}
        for e in connections:
            if e[0] in outEdges:
                outEdges[e[0]].append(e[1])
            else:
                outEdges[e[0]] = [e[1]]
            if e[1] in inEdges:
                inEdges[e[1]].append(e[0])
            else:
                inEdges[e[1]] = [e[0]]
        def DFS(v, visited):
            visited.add(v)
            if v in outEdges:
                for i in outEdges[v]:
                    if i not in visited:
                        r[0] += 1
                        DFS(i, visited)
            if v in inEdges:
                for i in inEdges[v]:
                    if i not in visited:
                        DFS(i, visited)
        DFS(0, set())
        return r[0]
        

a = Solution2()
# print(a.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
# print(a.minReorder(5, [[1,0],[1,2],[3,2],[3,4]]))
print(a.minReorder(10, [[0,1],[2,1],[3,2],[0,4],[5,1],[2,6],[5,7],[3,8],[8,9]]))