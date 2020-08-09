from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        r = []
        maxRow = len(nums[0])
        for n in range(1, len(nums)+1):
            for i in range(n):
                if len(nums[n-1]) > maxRow:
                    maxRow = len(nums[n])
                if i < len(nums[n-1-i]):
                    r.append(nums[n-1-i][i])
        rowLength = len(nums) - 1
        for n in reversed(range(1,maxRow)):
            for i in range(n):
                print(rowLength-i, (rowLength-n)+1+i)
                if rowLength-i > 0 and (rowLength-n)+1+i < len(nums[rowLength-i]):
                    r.append(nums[rowLength-i][(rowLength-n)+1+i])
        return r

a = Solution()
# print(a.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(a.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
print(a.findDiagonalOrder([[1,2,3,4,5,6]]))