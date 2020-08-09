from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[] for i in range(len(nums))]
        dp[0] = [nums[0]]
        for i in range(1, len(nums)):
            dp[i] = [nums[i]]
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j].copy()
                    dp[i].append(nums[i])
        r_index = 0
        r_max = 0
        for i, li in enumerate(dp):
            if len(li) > r_max:
                r_max = len(li)
                r_index = i
        return dp[r_index]

a = Solution()
a.largestDivisibleSubset([1,2,4,8])
