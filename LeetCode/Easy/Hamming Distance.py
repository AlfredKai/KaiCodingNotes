class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n //= 2
        return count

a = Solution()
print(a.hammingDistance(1, 4))