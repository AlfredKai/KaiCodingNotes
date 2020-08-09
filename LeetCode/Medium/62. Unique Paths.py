class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        m -= 1
        n -= 1
        up = m+n
        upup = up
        times = min(m,n)
        min_n = times
        while times > 1:
            up -= 1
            times -= 1
            upup *= up
            min_n *= times
        return upup // min_n

a = Solution()
# print(a.uniquePaths(3,7))
print(a.uniquePaths(1,2))