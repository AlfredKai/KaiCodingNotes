class Solution:
    def maxScore(self, s: str) -> int:
        accuZeros = [0] * len(s)
        accuZeros[0] = 1 if s[0] == '0' else 0
        # review enumerate start from 1
        for i in range(1, len(s)):
            accuZeros[i] = accuZeros[i-1]
            if s[i] == '0':
                accuZeros[i] += + 1
        accuReverseOnes = [0] * len(s)
        accuReverseOnes[len(s)-1] = 1 if s[len(s)-1] == '1' else 0
        for i in reversed(range(len(s)-1)):
            accuReverseOnes[i] = accuReverseOnes[i+1]
            if s[i] == '1':
                accuReverseOnes[i] += 1
        # review
        # r = max(accuZeros[-1], accuReverseOnes[-1])
        r = 0
        print(accuZeros, accuReverseOnes, r)
        for i in range(len(s)-1):
            sum = accuZeros[i] + accuReverseOnes[i+1]
            if sum > r:
                r = sum
        return r

a = Solution()
# print(a.maxScore('011101'))
print(a.maxScore('00'))