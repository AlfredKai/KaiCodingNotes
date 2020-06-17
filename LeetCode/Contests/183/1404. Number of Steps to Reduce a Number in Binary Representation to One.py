class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        for i, c in enumerate(s):
            if c == '1':
                num += 2 ** (len(s)-i-1)

        count = 0
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            count += 1
        return count

a = Solution()
print(a.numSteps('1101'))
print(a.numSteps('10'))
print(a.numSteps('1'))