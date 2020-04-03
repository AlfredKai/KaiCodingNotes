from collections import deque

def bfs(graph, start):
    visited, que = [start], deque(start)
    while que:
        v = que.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                que.append(w)
    return visited

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.append(v)
        for w in graph[v]:
            if w not in visited:
                stack.append(w)
    return visited

def dfs_recursion(graph, v, visited):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            dfs_recursion(graph, w, visited)


G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(bfs(G, 'A'))
print(dfs(G, 'A'))
visited = []
dfs_recursion(G, 'A', visited)
print(visited)

#      0  1  2  3  4  5  6
G2 = [[1, 1, 1, 0, 0, 0, 0], #0
      [1, 0, 0, 1, 1, 0, 0], #1
      [1, 0, 0, 0, 1, 0, 0], #2
      [0, 1, 0, 0, 0, 1, 0], #3
      [0, 1, 1, 0, 0, 1, 0], #4
      [0, 0, 0, 1, 1, 0, 1], #5
      [0, 0, 0, 0, 0, 1, 0]] #6