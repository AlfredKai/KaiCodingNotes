from typing import List

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adjMat = [[0]*(N+1) for i in range(N+1)]
        for edge in dislikes:
            adjMat[edge[0]][edge[1]] = 1
            adjMat[edge[1]][edge[0]] = 1
        
        self.r = True
        self.all = set()
        def DFS(mat, visit, visited, length, parent):
            visited[visit] = length
            self.all.add(visit)
            for i, n in enumerate(mat[visit]):
                if n == 1:
                    if i not in visited:
                        DFS(mat, i, visited, length+1, visit)
                    elif (length-visited[i]+1) % 2 == 1 and i != parent:
                        self.r = False
        
        for i in range(1,N+1):
            if i not in self.all:
                DFS(adjMat, i, {}, 1, 0)
        return self.r

a = Solution()
print(a.possibleBipartition(4, [[1,2],[1,3],[2,4]]))
print(a.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))
print(a.possibleBipartition(10, [[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]))