class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        r_most = n & -n
        return n - r_most == 0