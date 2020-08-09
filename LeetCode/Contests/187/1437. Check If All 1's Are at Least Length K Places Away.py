from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        r = True
        first = True
        count = 0
        while i < len(nums):
            if nums[i] == 1:
                if first:
                    first = False
                elif count < k:
                    r = False
                    break
                count = 0
                i+=1
                continue
            count += 1
            i+=1
        return r

a = Solution()
print(a.kLengthApart([1,0,0,1,0,1],2))
print(a.kLengthApart([1,0,0,0,1,0,0,1],2))
print(a.kLengthApart([1,1,1,1,1],0))
print(a.kLengthApart([0,1,0,1],1))
