class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        mbit = []
        while m > 0:
            mbit.append(m%2)
            m //= 2
        nbit = []
        while n > 0:
            nbit.append(n%2)
            n //= 2
        if len(mbit) != len(nbit):
            return 0
        r = 0
        for i in reversed(range(len(mbit))):
            if mbit[i] == nbit[i] and mbit[i] == 1:
                r += 2 ** (i)
            elif mbit[i] != nbit[i]:
                break
        return r



a = Solution()
print(a.rangeBitwiseAnd(129,160))
