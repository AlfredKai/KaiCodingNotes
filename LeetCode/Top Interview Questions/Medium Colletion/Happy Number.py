class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while True:
            r = 0
            while n > 0:
                r += (n % 10) ** 2
                n = int(n / 10)
            if r == 1:
                return True
            n = r
            if n in nums:
                return False
            nums.add(n)

a = Solution()

a.isHappy(19)