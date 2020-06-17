from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        indexBase = 0
        r = [-1, -1]
        while len(nums) > 0:
            l = len(nums)
            if nums[l//2] == target:
                r = [l//2 + indexBase, l//2 + indexBase]
                nLeft = nums[:l//2]
                nRight = nums[l//2:]
                leftBase = indexBase
                rightBase = l//2 + indexBase
                while len(nLeft) > 0:
                    lLeft = len(nLeft)
                    if nLeft[lLeft//2] == target:
                        r[0] = lLeft//2 + leftBase
                        nLeft = nLeft[:lLeft//2]
                    else:
                        if lLeft == 1:
                            break
                        nLeft = nLeft[lLeft//2:]
                        leftBase += lLeft//2
                while len(nRight) > 0:
                    lRight = len(nRight)
                    if nRight[lRight//2] == target:
                        if lRight == 1:
                            break
                        r[1] = lRight//2 + rightBase
                        nRight = nRight[lRight//2:]
                        rightBase += lRight//2
                    else:
                        nRight = nRight[:lRight//2]
                return r
            elif nums[l//2] < target:
                if l == 1:
                    break
                nums = nums[l//2:]
                indexBase += l//2
            else:
                nums = nums[0:l//2]
        return r

a = Solution()
print(a.searchRange([5,7,7,8,8,10], 8))
print(a.searchRange([5,7,7,8,8,10], 6))
print(a.searchRange([1,2,2,3,4,4,4], 4))
print(a.searchRange([2,2], 2))
print(a.searchRange([1], 1))