# Kai Coding Notes

[MkDocs](https://www.mkdocs.org/user-guide/configuration/)

## Tips

### Counting Problems

When a problem asks for the count (number) or max value, always be sensitive to time complexity. Even if a brute-force approach is O(n³) or O(2ⁿ), if it's just about counting, there's usually a way to optimize it down to O(n). Common strategies include:

- Reusing results from the previous step
- Dynamic Programming (DP)
- Some clever rule or pattern that avoids brute-force entirely

### In 2D DP, the value at `A[i][j]` is typically derived from:

- `A[i-1][j]`
- `A[i][j-1]`
- `A[i-1][j-1]`

### Permutations

- When the problem involves permutations, think of using a `Counter`.

### Binary Search

- If the data is sorted, consider whether binary search applies.
- If sorted data is involved and the required complexity is O(n log n), it's almost certainly a binary search problem (99.9%).

### Time Complexity Intuition

- If the output requires listing all results, it’s likely a brute-force problem solvable via backtracking.

### DP Intuition

- When you see a matrix or array, think: "Can this be solved with DP?"
