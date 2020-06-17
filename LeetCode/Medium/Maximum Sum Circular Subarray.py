from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 1:
            return A[0]
        cumMaxRight = [0] * len(A)
        cumMaxRight[0] = A[0]
        for i in range(1, len(A)):
            cumMaxRight[i] = max(A[i], cumMaxRight[i-1] + A[i])
        sumAll = sum(A)
        dp = [0] * (len(A)-1)
        dp[-1] = sumAll
        for i in reversed(range(len(dp)-1)):
            dp[i] = max(dp[i+1] - A[i+1], sumAll)
        return max(max(cumMaxRight), max(dp))

a = Solution()
print(a.maxSubarraySumCircular([1,-2,3,-2]))
print(a.maxSubarraySumCircular([-2,-3,-1]))
print(a.maxSubarraySumCircular([-2]))