# Shortest path

- Single Source Shortest Path
  - Dijkstra
    - `O((|V|+|E|)log|V|)`
    - directed graphs with unbounded non-negative weights
  - Bellman-Ford
    - `O(|V||E|)`
    - can detect and report the negative cycle
- All pairs shortest paths
  - Floyd-Warshall
    - `O(|V|^3)`
    - weighted graph with positive or negative edge weights (but with no negative cycles)
