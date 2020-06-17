from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        halfSumf = sum(nums) / 2
        curSum = 0
        r = []
        for n in nums:
            curSum += n
            r.append(n)
            if curSum > halfSumf:
                break
        return r

a = Solution()
print(a.minSubsequence([7,4,2,8,1,7,7,10]))