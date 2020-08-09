class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return '1'
        nlist = [i for i in range(1, n+1)]
        r = ''
        n_f = 1
        for i in range(1, n+1):
            n_f *= i
        while True:
            if len(nlist) == 2:
                if k == 1:
                    r += str(nlist[0]) + str(nlist[1])
                    break
                elif k == 0 or k == 2:
                    r += str(nlist[1]) + str(nlist[0])
                    break
            n_f //= n
            n -= 1
            select = nlist[(k-1)//n_f]
            del nlist[(k-1)//n_f]
            k %= n_f
            r += str(select)
        return r

a = Solution()
# print(a.getPermutation(4, 3))
# print(a.getPermutation(3, 1))
print(a.getPermutation(3, 2))
# print(a.getPermutation(2, 2))
