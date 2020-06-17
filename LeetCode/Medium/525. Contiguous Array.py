from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sumNums = [0] * (len(nums) + 1)
        for i, n in enumerate(nums, 1):
            if n == 0:
                a = -1
            else:
                a = 1
            sumNums[i] = a + sumNums[i-1]
        sumPos = {}
        maxLen = 0
        for i in range(len(sumNums)):
            if sumNums[i] not in sumPos:
                sumPos[sumNums[i]] = i
            else:
                if i - sumPos[sumNums[i]] > maxLen:
                    maxLen = i - sumPos[sumNums[i]]
        return maxLen

class Solution2:
    def findMaxLength(self, nums: List[int]) -> int:
        rec = {0:-1}
        balance = 0
        r = 0
        for i, n in enumerate(nums):
            if n == 1:
                balance += 1
            else:
                balance -= 1

            if balance not in rec:
                rec[balance] = i
            else:
                r = max(r,i - rec[balance])
        return r
    
a = Solution()
print(a.findMaxLength([0,1]))