class Solution2:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        pivot = 0
        remove_index = set()
        while k > 0:
            if k == len(num) - pivot:
                for i in range(pivot, len(num)):
                    remove_index.add(i)
                break
            min_index = pivot
            for i in range(pivot+1, pivot+k+1):
                if int(num[i]) < int(num[min_index]):
                    min_index = i
            if min_index == pivot:
                pivot += 1
            else:
                k -= min_index - pivot
                for i in range(pivot, min_index):
                    remove_index.add(i)
                pivot = min_index
        r = ''
        firstDigit = True
        for i, n in enumerate(num):
            if i not in remove_index:
                if firstDigit and n == '0':
                    continue
                r += n
                firstDigit = False
        return r if len(r) != 0 else '0'

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        r = num[0]
        for i in range(1, len(num)):
            if int(num[i]) < int(num[i-1]) and k > 0:
                r = r[:-1] + num[i]
                k -= 1
            else:
                r += num[i]
        else:
            if k > 0:
                r = r[:-k]
            if not r:
                return '0'
            for i, n in enumerate(r):
                if n != '0':
                    break
            r = r[i:]
        return r




a = Solution()
print(a.removeKdigits('1432219',3))
print(a.removeKdigits('10200',1))
print(a.removeKdigits('10',2))
print(a.removeKdigits('1234',3))
print(a.removeKdigits('9',1))
print(a.removeKdigits('1234567890', 9))