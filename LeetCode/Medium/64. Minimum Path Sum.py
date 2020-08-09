from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        dp = [[0] * col for i in range(row)]
        for i in range(0, row):
            for j in range(0, col):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue
                if i == 0:
                    dp[i][j] += grid[i][j] + dp[i][j-1]
                    continue
                if j == 0:
                    dp[i][j] += grid[i][j] + dp[i-1][j]
                    continue
                dp[i][j] += grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                
                # print(dp[0])
                # print(dp[1])
                # print(dp[2])
        return dp[row-1][col-1]

a = Solution()
# a.minPathSum([
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ])
a.minPathSum([
    [1,3,1],
    [1,5,1],
    [4,2,1]
])