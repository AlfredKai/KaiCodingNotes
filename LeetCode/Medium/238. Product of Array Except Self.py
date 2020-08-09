from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 1 :
            return [0]
        r = [1] * len(nums)
        for i in range(1, len(nums)):
            r[i] = nums[i-1] * r[i-1]
        temp = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            r[i] = r[i] * temp
            temp = nums[i] * temp
        return r

a = Solution()
print(a.productExceptSelf([1,2,3,4]))