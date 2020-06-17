class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def _climbStairs(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            if n in cache:
                return cache[n]
            else:
                cache[n] = _climbStairs(n - 1) + _climbStairs(n - 2)

            return cache[n]
        return _climbStairs(n)

a = Solution()
print(a.climbStairs(2)) # expect 2
print(a.climbStairs(3)) # expect 3