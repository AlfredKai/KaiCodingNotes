from typing import List

class Solution2:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxNum = 1000000001
        minNum = 0
        r = 0
        for i in range(len(nums)):
            maxNum = nums[i]
            minNum = nums[i]
            for j in range(i,len(nums)):
                maxNum = max(maxNum, nums[j])
                minNum = min(minNum, nums[j])
                if maxNum - minNum <= limit:
                    r = max(r, j - i + 1)
        return r

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result = 0
        curMax = [0] * len(nums)
        curMax[0] = nums[0]
        curMin = [0] * len(nums)
        curMin[0] = nums[0]
        for i in range(i, len(nums)):
            curMax[i] = max(curMax[i], curMax[i-1])
            curMin[i] = min(curMin[i], curMin[i-1])
        j = 0
        i = 0
        while j < len(nums):
            nowMax = curMax[j-1] - 
            if j-1 >= 0:
                if abs(nums[j], curMax[j-1]) <= limit and abs(nums[j], curMin[j-1]) <= limit:
                    result = max(result, j-i+1)
            else:
                if limit == 0:
                    result = max(result, 1)
                i += 1
            j += 1
        return result

a = Solution()
print(a.longestSubarray([8,2,4,7],4))
# print(a.longestSubarray([10,1,2,4,7,2],5))
# print(a.longestSubarray([4,2,2,2,4,4,2,2],0))
