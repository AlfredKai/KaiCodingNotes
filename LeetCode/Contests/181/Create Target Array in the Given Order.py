from typing import List

# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        r = []
        for i in range(0, len(nums)):
            r.append(nums[i])
            if index[i] < len(r):
                for j in range(len(r)-1, index[i], -1):
                    t = r[j]
                    r[j] = r[j-1]
                    r[j-1] = t
        return r

a = Solution()
print(a.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))
print(a.createTargetArray([1,2,3,4,0], [0,1,2,3,0]))