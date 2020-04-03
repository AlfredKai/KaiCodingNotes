from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if len(grid) == 1 and len(grid[0]) == 1:
            return True
        if grid[0][0] == 5:
            return False

        def checkMatch(cur, next, dir) -> bool:
            checker = {
                1:{
                    1:{
                        'u': False,
                        'b': False,
                        'l': True,
                        'r': True
                    },
                    2:{
                        'u': False,
                        'b': False,
                        'l': False,
                        'r': False
                    },
                    3:{
                        'u': False,
                        'b': False,
                        'l': False,
                        'r': True
                    },
                    4:{
                        'u': False,
                        'b': False,
                        'l': True,
                        'r': False
                    },
                    5:{
                        'u': False,
                        'b': False,
                        'l': False,
                        'r': True
                    },
                    6:{
                        'u': False,
                        'b': False,
                        'l': True,
                        'r': False
                    },
                },
                2:{
                    1:{
                        'u': False,
                        'b': False,
                        'l': False,
                        'r': False
                    },
                    2:{
                        'u': True,
                        'b': True,
                        'l': False,
                        'r': False
                    },
                    3:{
                        'u': True,
                        'b': False,
                        'l': False,
                        'r': False
                    },
                    4:{
                        'u': True,
                        'b': False,
                        'l': False,
                        'r': False
                    },
                    5:{
                        'u': False,
                        'b': True,
                        'l': False,
                        'r': False
                    },
                    6:{
                        'u': False,
                        'b': True,
                        'l': False,
                        'r': False
                    },
                },
                3:{
                    1:{
                        'u': False,
                        'b': False,
                        'l': True,
                        'r': False
                    },
                    2:{
                        'u': False,
                        'b': True,
                        'l': False,
                        'r': False
                    },
                    3:{
                        'u': False,
                        'b': False,
                        'l': False,
                        'r': False
                    },
                    4:{
                        'u': False,
                        'b': False,
                        'l': True,
                        'r': False
                    },
                    5:{
                        'u': False,
                        'b': True,
                        'l': False,
                        'r': False
                    },
                    6:{
                        'u': False,
                        'b': True,
                        'l': False,
                        'r': False
                    },
                },
                4:{
                    1:{
                        'u': False,
                        'b': False,
                        'l': False,
                        'r': True
                    },
                    2:{
                        'u': False,
                        'b': True,
                        'l': False,
                        'r': False
                    },
                    3:{
                        'u': False,
                        'b': False,
                        'l': False,
                        'r': True
                    },
                    4:{
                        'u': False,
                        'b': False,
                        'l': False,
                        'r': False
                    },
                    5:{
                        'u': False,
                        'b': True,
                        'l': False,
                        'r': True
                    },
                    6:{
                        'u': False,
                        'b': True,
                        'l': False,
                        'r': False
                    },
                },
                5:{
                    1:{
                        'u': False,
                        'b': False,
                        'l': True,
                        'r': False
                    },
                    2:{
                        'u': True,
                        'b': False,
                        'l': False,
                        'r': False
                    },
                    3:{
                        'u': True,
                        'b': False,
                        'l': False,
                        'r': False
                    },
                    4:{
                        'u': True,
                        'b': False,
                        'l': True,
                        'r': False
                    },
                    5:{
                        'u': False,
                        'b': False,
                        'l': False,
                        'r': False
                    },
                    6:{
                        'u': False,
                        'b': False,
                        'l': True,
                        'r': False
                    },
                },
                6:{
                    1:{
                        'u': False,
                        'b': False,
                        'l': False,
                        'r': True
                    },
                    2:{
                        'u': True,
                        'b': False,
                        'l': False,
                        'r': False
                    },
                    3:{
                        'u': True,
                        'b': False,
                        'l': True,
                        'r': False
                    },
                    4:{
                        'u': True,
                        'b': False,
                        'l': False,
                        'r': False
                    },
                    5:{
                        'u': False,
                        'b': False,
                        'l': False,
                        'r': True
                    },
                    6:{
                        'u': False,
                        'b': False,
                        'l': False,
                        'r': False
                    },
                },
            }
            return checker[cur][next][dir]
        # m: row n: col
        # 
        def checkNextDir(cur, index, dir) -> tuple:
            checker = {
                1: {
                    'u': False,
                    'b': False,
                    'l': (index[0], index[1]-1, 'l'),
                    'r': (index[0], index[1]+1, 'r')
                },
                2: {
                    'u': (index[0]-1, index[1], 'u'),
                    'b': (index[0]+1, index[1], 'b'),
                    'l': False,
                    'r': False
                },
                3: {
                    'u': (index[0], index[1]-1, 'l'),
                    'b': False,
                    'l': False,
                    'r': (index[0]+1, index[1], 'b')
                },
                4: {
                    'u': (index[0], index[1]+1,'r'),
                    'b': False,
                    'l': (index[0]+1, index[1],'b'),
                    'r': False
                },
                5: {
                    'u': False,
                    'b': (index[0], index[1]-1, 'l'),
                    'l': False,
                    'r': (index[0]-1, index[1], 'u')
                },
                6: {
                    'u': False,
                    'b': (index[0], index[1]+1, 'r'),
                    'l': (index[0]-1, index[1], 'u'),
                    'r': False
                },
            }
            return checker[cur][dir]
        firstDir = {
            1: 'r',
            2: 'b',
            3: 'r',
            6: 'b'
        }
        def checkPath(grid, dir):
            m = len(grid)
            n = len(grid[0])
            r = c = 0
            while r != m - 1 or c != n - 1:
                print(r, c, grid[r][c])
                next = checkNextDir(grid[r][c], (r,c), dir)
                if next[0] > m - 1 or next[1] > n - 1 or next[0] < 0 or next[1] < 0:
                    return False
                if not checkMatch(grid[r][c], grid[next[0]][next[1]], next[2]):
                    return False
                r = next[0]
                c = next[1]
                dir = next[2]
            return True
        if grid[0][0] != 4:
            dir = firstDir[grid[0][0]]
            return checkPath(grid,dir)
        else:
            return checkPath(grid,'u') or checkPath(grid,'l')

class Solution2:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        connections = {
            1: {
                'u': False,
                'b': False,
                'l': True,
                'r': True,
            },
            2: {
                'u': True,
                'b': True,
                'l': False,
                'r': False,
            },
            3: {
                'u': False,
                'b': True,
                'l': True,
                'r': False,
            },
            4: {
                'u': False,
                'b': True,
                'l': False,
                'r': True,
            },
            5: {
                'u': True,
                'b': False,
                'l': True,
                'r': False,
            },
            6: {
                'u': True,
                'b': False,
                'l': False,
                'r': True,
            },
        }
        def getNeibor(v):
            neibors = []
            r = v[0]
            c = v[1]
            if r > 0: # u
                if connections[grid[r][c]]['u'] and connections[grid[r-1][c]]['b']:
                    neibors.append((r-1,c))
            if r < len(grid)-1: # b
                if connections[grid[r][c]]['b'] and connections[grid[r+1][c]]['u']:
                    neibors.append((r+1,c))
            if c > 0: # l
                if connections[grid[r][c]]['l'] and connections[grid[r][c-1]]['r']:
                    neibors.append((r,c-1))
            if c < len(grid[r])-1: # r
                if connections[grid[r][c]]['r'] and connections[grid[r][c+1]]['l']:
                    neibors.append((r,c+1))
            return neibors

        def dfs(g, v, visited):
            visited.add(v)
            for w in getNeibor(v):
                if w not in visited:
                    dfs(g, w, visited)

        visited = set()
        dfs(grid, (0, 0), visited)
        return (len(grid)-1, len(grid[0])-1) in visited

a = Solution()
print(a.hasValidPath([[2,4,3],[6,5,2]]))
print(a.hasValidPath([[1,2,1],[1,2,1]]))
print(a.hasValidPath([[1,1,2]]))
print(a.hasValidPath([[1,1,1,1,1,1,3]]))
print(a.hasValidPath([[2],[2],[2],[2],[2],[2],[6]]))
print(a.hasValidPath([[1,1,1,1,6],[1,1,1,1,2],[1,1,1,1,2],[1,1,1,1,2],[1,1,1,1,2]]))
print(a.hasValidPath([[4,1],[6,1]]))
print(a.hasValidPath([[6,1,3],[4,1,5]]))
print(a.hasValidPath([[3,4,3,4],[2,2,2,2],[6,5,6,5]]))