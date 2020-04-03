class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        powOf3 = 3
        while powOf3 <= n:
            if powOf3 == n:
                return True
            powOf3 *= 3
        return False

a = Solution()
print(a.isPowerOfThree(27))
print(a.isPowerOfThree(0))
print(a.isPowerOfThree(9))
print(a.isPowerOfThree(45))