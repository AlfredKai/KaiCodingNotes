from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

a = Solution()
print(a.findKthLargest([3,2,1,5,6,4], 2))