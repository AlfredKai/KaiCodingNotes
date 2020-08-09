from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        r = []
        for i in range(n):
            r.append(nums[i])
            r.append(nums[i+n-1])
        return r

a = Solution()
a.shuffle([2,5,1,3,4,7], 3)