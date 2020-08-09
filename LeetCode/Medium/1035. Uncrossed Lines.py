from typing import List

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * len(B) for i in range(len(A))]
        r = 0
        dp[0][0] = 1 if A[0] == B[0] else 0
        for i in range(1, len(A)):
            dp[i][0] = 1 if A[i] == B[0] else dp[i-1][0]
        for i in range(1, len(B)):
            dp[0][i] = 1 if B[i] == A[0] else dp[0][i-1]
        r = max(dp[0])
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                r = max(r, dp[i][j])
        return r

a = Solution()
print(a.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))