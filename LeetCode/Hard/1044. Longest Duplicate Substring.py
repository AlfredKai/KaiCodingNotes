from collections import Counter

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def check_size(size):
            hash = set()
            hash.add(S[:size])
            for i in range(1, len(S) - size + 1):
                temp = S[i:i+size]
                if temp in hash:
                    return S[i:i+size]
                else:
                    hash.add(temp)
            return ''
        n = len(S)
        i = 0
        j = n - 1
        while i <= j:
            mid = (i+j)//2
            if len(check_size(mid)) > 0:
                i = mid
                if i + 1 == j:
                    r = check_size(j)
                    if len(r) > 0:
                        return r
                    else:
                        return check_size(i)
            else:
                j = mid
                if i + 1 == j:
                    r = check_size(mid-1)
                    if len(r) > 0:
                        return r
                    else:
                        return check_size(mid-2)
                if i == j:
                    return check_size(mid-1)

a = Solution()
print(a.longestDupSubstring('abcd'))
print(a.longestDupSubstring('banana'))