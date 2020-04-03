class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for x in range(len(text2))] for y in range(len(text1))]

        def printMemo(memo):
            for a in memo:
                for b in a:
                    print(b, end=' ')
                print('')
            print('')

        def memoLCS(i, j, memo):
            print(i, j)
            printMemo(memo)
            if i == 0: 
                memo[i][j] = 1 if text1[i] in text2[:j+1] else 0
                return memo[i][j]
            if j == 0:
                memo[i][j] = 1 if text2[j] in text1[:i+1] else 0
                return memo[i][j]

            if text1[i] == text2[j]:
                if memo[i-1][j-1] != -1:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = memoLCS(i-1, j-1, memo) + 1
                return memo[i][j]
            else:
                if memo[i][j-1] == -1:
                    memo[i][j-1] = memoLCS(i, j-1, memo)
                if memo[i-1][j] == -1:
                    memo[i-1][j] = memoLCS(i-1, j, memo)
                if memo[i][j-1] > memo[i-1][j]:
                    return memo[i][j-1]
                else:
                    return memo[i-1][j]
        return memoLCS(len(text1) - 1, len(text2) - 1, dp)

a = Solution()
# print(a.longestCommonSubsequence('abcde', 'ace'))
print(a.longestCommonSubsequence('abc', 'dbf'))
# print(a.longestCommonSubsequence('abc', 'abc'))
# print(a.longestCommonSubsequence('abc', 'def'))
# print(a.longestCommonSubsequence('ezupkr', 'ubmrapg'))
# print(a.longestCommonSubsequence('abcde', 'fgaij'))
# print(a.longestCommonSubsequence('abcbdab', 'bdcaba'))