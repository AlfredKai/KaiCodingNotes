from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        i = 0
        N = len(citations)
        j = N - 1
        while i <= j:
            mid = (i+j)//2
            h = (N-mid)
            if citations[mid] >= h:
                j = mid
                if i >= j:
                    return h
            else:
                i = mid
                if i+1 == j:
                    if citations[i+1] >= h - 1:
                        return h - 1
                    else:
                        return h - 2
                elif i == j:
                    return h - 1

a = Solution()
print(a.hIndex([0,1,3,5,6]))
print(a.hIndex([10,11,12,13,14,15,16,17]))
print(a.hIndex([]))
print(a.hIndex([0]))
print(a.hIndex([1]))
print(a.hIndex([100]))
print(a.hIndex([0,0,0,0,0,0]))
print(a.hIndex([0,0]))
print(a.hIndex([1,1]))