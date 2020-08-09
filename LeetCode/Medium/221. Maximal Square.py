from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        found = False
        hasZero = False
        smallEdge = min(len(matrix), len(matrix[0]))
        for size in reversed(range(1, smallEdge+1)):
            for i in range(0, len(matrix)-size+1):
                for j in range(0, len(matrix[0])-size+1):
                    # square check
                    # print(i,j)
                    hasZero = False
                    for m in range(i, i+size):
                        for n in range(j,j+size):
                            if matrix[m][n] == '0':
                                hasZero = True
                                break
                        if hasZero:
                            break
                    else:
                        if not hasZero:
                            found = True
                if found:
                    break
            if found:
                break
        return size * size if found else 0

class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[[0,0,0] for j in range(col)] for i in range(row)]
        r = 0
        for m in range(row):
            for n in range(col):
                val = matrix[m][n]
                valDp = dp[m][n]
                if val == '1':
                    if n - 1 >= 0 and m - 1 >= 0:
                        valDp[2] = min(dp[m-1][n-1][2]+1, dp[m-1][n][0]+1, dp[m][n-1][1]+1)
                    else:    
                        valDp[2] = 1
                    if m - 1 >= 0:
                        valDp[0] += dp[m-1][n][0]
                    valDp[0] += 1

                    if n - 1 >= 0:
                        valDp[1] += dp[m][n-1][1]
                    valDp[1] += 1
                r = max(r, valDp[2])
        return r * r

a = Solution2()
# print(a.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
# print(a.maximalSquare([])
# print(a.maximalSquare([["0","1"]]))
print(a.maximalSquare([["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]))