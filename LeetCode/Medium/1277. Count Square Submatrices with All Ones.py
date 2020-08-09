from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        r = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                for size in range(1, min(m, n)+1):
                    if i+size > m or j+size >n:
                        break
                    skip = False
                    for k in range(i, i+size):
                        for l in range(j, j+size):
                            if matrix[k][l] != 1:
                                skip = True
                                break
                        if skip:
                            break
                    else:
                        r += 1
        return r

class Solution2:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * col for i in range(row)]
        r = 0
        for m in range(row):
            for n in range(col):
                if m == 0:
                    dp[m][n] = matrix[m][n]
                    r += dp[m][n]
                    continue
                if n == 0:
                    dp[m][n] = matrix[m][n]
                    r += dp[m][n]
                    continue
                if matrix[m][n] == 1:
                    dp[m][n] = min(dp[m-1][n], dp[m][n-1], dp[m-1][n-1]) + 1
                    r += dp[m][n]
        return r       

a = Solution2()
# print(a.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
print(a.countSquares([[1,0,1],[1,1,0],[1,1,0]]))