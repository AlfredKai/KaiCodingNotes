class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        numList = [1] * n
        numList[0] = 0
        numList[1] = 0
        for curNum in range(2, n):
            if numList[curNum] == 0:
                continue
            for checkNum in range(curNum*curNum, n, curNum):
                numList[checkNum] = 0
        return sum(numList)

a = Solution()
print(a.countPrimes(2))
print(a.countPrimes(3))
print(a.countPrimes(5))
print(a.countPrimes(10))
print(a.countPrimes(100))
