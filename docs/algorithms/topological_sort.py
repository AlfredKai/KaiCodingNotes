# Kahn’s algorithm
from typing import List
from collections import defaultdict

def topological_sort(graph: defaultdict, n: int) -> List:
    in_degree = [0] * n
    for i in graph:
        for j in graph[i]:
            in_degree[j] += 1

    zero_in_deg = []
    for i in range(n):
        if in_degree[i] == 0:
            zero_in_deg.append(i)

    r = []
    while zero_in_deg:
        v = zero_in_deg.pop()
        r.append(v)
        for i in graph[v]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                zero_in_deg.append(i)
    
    return r

a = defaultdict(list)
a[5] = [2]
a[5].append(0)
a[4] = [0]
a[4].append(1)
a[2] = [3]
a[3] = [1]
b = topological_sort(a, 6)
print(b)