from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.front = [0]
        self.end = [0] * len(nums)
        self.total = sum(nums)
        for i in range(1, len(nums)):
            self.front.append(self.front[i-1] + nums[i-1])
        for i in range(len(nums) - 2, -1, -1):
            self.end[i] = self.end[i+1] + nums[i+1]
        print('front', self.front)
        print('end', self.end)
        # front [0, -2, -2, 1, -4, -2]
        # end [-1, -1, -4, 1, -1, 0]

    def sumRange(self, i: int, j: int) -> int:
        return self.total - self.front[i] - self.end[j]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
obj = NumArray([-2,0,3,-5,2,-1])
print(obj.sumRange(2,5))