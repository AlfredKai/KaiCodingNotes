from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        rec = [0] * len(rating)
        ascDscRec = {rating[0]:[0,0]}
        for i in range(1, len(rating)):
            ascDscRec[rating[i]] = [0, 0]
            for j in range(0, i):
                if rating[i] > rating[j]:
                    ascDscRec[rating[i]][0] += 1
                    rec[i] += ascDscRec[rating[j]][0]
                else:
                    ascDscRec[rating[i]][1] += 1
                    rec[i] += ascDscRec[rating[j]][1]
            rec[i] += rec[i-1]
        return rec[-1]

class Solution2:
    def numTeams(self, rating: List[int]) -> int:
        for i in range(0, len(rating)-2):
            for j in range(i+1, len(rating)-1):
                for k in range(j+1, len(rating)):
                    if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]:
                        count += 1
        return count

a = Solution()
print(a.numTeams([2,5,3,4,1]))

