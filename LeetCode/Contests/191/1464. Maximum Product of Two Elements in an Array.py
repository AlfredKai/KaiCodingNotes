from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (sorted(nums,reverse=True)[0] - 1) * (sorted(nums,reverse=True)[1]-1)