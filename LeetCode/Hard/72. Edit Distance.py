class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_len = len(word1)
        word2_len = len(word2)
        if not word1:
            return word2_len
        if not word2:
            return word1_len
        dp = [[0] * word2_len for i in range(word1_len)]
        dp[0][0] = 0 if word1[0] == word2[0] else 1
        flag = True
        for i in range(1, word2_len):
            dp[0][i] = dp[0][i-1]
            if word1[0] == word2[i] and flag:
                flag = False
                continue
            dp[0][i] += 1
        flag = True
        for i in range(1, word1_len):
            dp[i][0] = dp[i-1][0]
            if word1[i] == word2[0] and flag:
                flag = False
                continue
            dp[i][0] += 1
        for i in range(1, word1_len):
            for j in range(1, word2_len):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] =  min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[word1_len-1][word2_len-1]

a = Solution()
# print(a.minDistance("horse", "ros"))
# print(a.minDistance("intention", "execution"))
# print(a.minDistance("a", "a"))
# print(a.minDistance("a", "b"))
# print(a.minDistance("sea", "ate"))
# print(a.minDistance("algorithm", "altruistic"))
print(a.minDistance("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically"))