from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        r = []
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i = i+1
                continue
            if B[j][1] < A[i][0]:
                j = j+1
                continue
            if A[i][0] < B[j][0]:
                if A[i][1] < B[j][1]:
                    r.append([B[j][0], A[i][1]])
                    i += 1
                else:
                    r.append([B[j][0], B[j][1]])
                    j += 1
            else:
                if B[j][1] < A[i][1]:
                    r.append([A[i][0], B[j][1]])
                    j += 1
                else:
                    r.append([A[i][0], A[i][1]])
                    i += 1
        return r


a = Solution()
a.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])