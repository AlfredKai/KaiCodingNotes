from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(nums, isTaken):
            for i, n in enumerate(nums):
                if not isTaken[i]:
                    isTaken[i] = True
                    print(isTaken)
                    helper(nums, isTaken)
                    isTaken[i] = False
        helper(nums, [False] * len(nums))

a = Solution()
a.permute([1,2,3])