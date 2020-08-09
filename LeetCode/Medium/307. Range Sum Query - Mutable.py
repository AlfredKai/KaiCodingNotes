from typing import List

class FenwickTree:
    def __init__(self, arr):
        self.n = len(arr) + 1
        self.ft = [0] * (self.n)
        for i, v in enumerate(arr):
            self.update(i, v)

    def update(self, i, v):
        i += 1
        while i < self.n:
            self.ft[i] += v
            i += i & (-i)

    def query(self, i):
        i += 1
        r = 0
        while i > 0:
            r += self.ft[i] 
            i -= i & (-i)
        return r

class NumArray:

    def __init__(self, nums: List[int]):
        self.ft = FenwickTree(nums)
        self.org = nums

    def update(self, i: int, val: int) -> None:
        diff = val - self.org[i]
        self.org[i] = val
        self.ft.update(i,diff)
        

    def sumRange(self, i: int, j: int) -> int:
        lower = 0 if i == 0 else self.ft.query(i-1)
        return self.ft.query(j) - lower


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)