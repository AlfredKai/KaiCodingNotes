from typing import List

# bottom-up DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        memo = [0] * len(nums)
        memo[0] = nums[0]
        for i in range(1, len(nums)):
            memo[i] = max(nums[i], memo[i-1] + nums[i])
        return max(*memo)

a = Solution()
print(a.maxSubArray([1]))
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))