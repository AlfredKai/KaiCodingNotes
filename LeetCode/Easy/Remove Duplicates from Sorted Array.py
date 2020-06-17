from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        cur = 0
        stopFlag = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if not stopFlag:
                    stopFlag = 1
                    cur += 1
            else:
                if stopFlag:
                    nums[cur] = nums[i]
                    stopFlag = 0
                else:
                    cur += 1
                    nums[cur] = nums[i]
        return cur if stopFlag else cur + 1

b = [0,0,1,1,1,2,2,3,3,4]
a = Solution()
print(a.removeDuplicates(b))
print(b)
print()
b = [1,2]
print(a.removeDuplicates(b))
print(b)
print()
b = [1,1]
print(a.removeDuplicates(b))
print(b)
print()
b = [1,2,2]
print(a.removeDuplicates(b))
print(b)