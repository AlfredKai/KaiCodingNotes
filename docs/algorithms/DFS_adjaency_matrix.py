from typing import List

def DFS(graph: List[List[int]]):
    stack = [0]
    visited = set()
    v = stack[0]
    while len(stack) > 0:
        visited.add(v)
        for connected_v in range(0, len(graph)):
            if connected_v in visited:
                continue
            if graph[v][connected_v] == 1:
                print('visited: ', visited)
                stack.append(connected_v)
                v = connected_v
                break
        else:
            v = stack.pop()
            print(v)
    return 0

def DFSRecursive(graph:List[List[int]], start, visited: List):
    

#         0  1  2  3  4  5  6
graph = [[1, 1, 1, 0, 0, 0, 0], #0
         [1, 0, 0, 1, 1, 0, 0], #1
         [1, 0, 0, 0, 1, 0, 0], #2
         [0, 1, 0, 0, 0, 1, 0], #3
         [0, 1, 1, 0, 0, 1, 0], #4
         [0, 0, 0, 1, 1, 0, 1], #5
         [0, 0, 0, 0, 0, 1, 0]] #6

DFS(graph)
