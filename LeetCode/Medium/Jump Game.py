from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        check = [0 for i in range(0, len(nums))]
        if nums[0] > 0:
            check[0] = 1
            check[1] = 1
        else:
            return False
        for i in range(1, len(nums)):
            for j in range(i, -1, -1):
                if check[j] == 1 and nums[j] + j >= i:
                    check[i] = 1
                    break
        return check[len(nums) - 1] == 1

# after 9 month later
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        curSmallIndex = len(nums) - 1
        for i in reversed(range(len(nums)-1)):
            if curSmallIndex - i <= nums[i]:
                curSmallIndex = i
        return curSmallIndex == 0

a = Solution()
print(a.canJump([2,3,1,1,4]))
# assert a.canJump([2,3,1,1,4]) == True

print(a.canJump([3,2,1,0,4]))
# assert a.canJump([3,2,1,0,4]) == False

print(a.canJump([2, 0, 0]))
# assert a.canJump([2, 0, 0]) == True