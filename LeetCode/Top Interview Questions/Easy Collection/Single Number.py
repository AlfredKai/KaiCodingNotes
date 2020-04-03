from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rec = {}
        for i in range(0, len(nums)):
            if nums[i] not in rec:
                rec[nums[i]] = 1
            else:
                rec[nums[i]] += 1
        for i in rec:
            if rec[i] == 1:
                return i