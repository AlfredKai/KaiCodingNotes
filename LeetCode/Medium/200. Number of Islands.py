from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        visited = [[0] * col for i in range(row)]
        def DFS(grid, pos, visited, group, connected):
            visited[pos[0]][pos[1]] = group
            if   pos[0] > 0 and grid[pos[0]-1][pos[1]] == connected and visited[pos[0]-1][pos[1]] != group:
                DFS(grid, (pos[0]-1, pos[1]), visited, group, connected)
            if pos[0] < row - 1 and grid[pos[0]+1][pos[1]] == connected and visited[pos[0]+1][pos[1]] != group:
                DFS(grid, (pos[0]+1, pos[1]), visited, group, connected)
            if pos[1] > 0 and grid[pos[0]][pos[1]-1] == connected and visited[pos[0]][pos[1]-1] != group:
                DFS(grid, (pos[0], pos[1]-1), visited, group, connected)
            if pos[1] < col - 1 and grid[pos[0]][pos[1]+1] == connected and visited[pos[0]][pos[1]+1] != group:
                DFS(grid, (pos[0], pos[1]+1), visited, group, connected)

        curGroup = 0
        for r in range(row):
            for c in range(col):
                if visited[r][c] == 0:
                    if grid[r][c] == '0':
                        group = -1
                    else:
                        curGroup += 1
                        group = curGroup
                    DFS(grid, (r, c), visited, group, grid[r][c])
        return curGroup


a = Solution()
# print(a.numIslands([
#     ['1','1','0','0','0'],
#     ['1','1','0','0','0'],
#     ['0','0','1','0','0'],
#     ['0','0','0','1','1'],
#     ]))
print(a.numIslands([
    ["1","1","1"],
    ["0","1","0"],
    ["0","1","0"]
    ]))
# print(a.numIslands([
#     ["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
#     ))