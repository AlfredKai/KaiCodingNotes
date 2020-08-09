# Graph

## DFS

```py
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
```
```py
def dfs_recursion(graph, v, visited):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            dfs_recursion(graph, w, visited)
```