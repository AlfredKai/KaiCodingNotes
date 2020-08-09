from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            # print(nums[l], nums[r], nums[mid])
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[l]:
                if nums[mid] > target:
                    r = mid - 1
                elif nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target:
                    l = mid + 1
                elif nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
    
    def 耍蠢紀念(self, nums: List[int], target: int):
        l = 0
        r = len(nums) - 1
        last = target
        first = True
        toRight = False
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            if not first and toRight and last > nums[mid]:
                r = mid - 1
                toRight = False
            elif not first and not toRight and last < nums[mid]:
                l = mid + 1
                toRight = True
            elif nums[mid] > target:
                r = mid - 1
                toRight = False
                last = nums[mid]
            else:
                l = mid + 1
                toRight = True
                last = nums[mid]
            first = False

        if l > len(nums) - 1:
            l = 0
            r = (len(nums) - 1 + l) // 2
            while l <= r:
                mid = (r + l) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < last:
                    r = mid - 1
                else:
                    if nums[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
        if r < 0:
            l = ((len(nums) - 1) // 2) + 1
            r = len(nums) - 1
            while l <= r:
                mid = (r + l) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > last:
                    l = mid + 1
                else:
                    if nums[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
        return -1

a = Solution()
print(a.search([5,6,7,1,2,3,4], 7))
print(a.search([4,5,6,7,8,1,2,3], 2))
print(a.search([4,5,6,7,8,1,2,3], 7))
print(a.search([4], 4))
print(a.search([3,1], 1))
print(a.search([4,5,6,7,8,1,2,3],8))
print(a.search([82,84,85,87,88,93,95,96,97,98,99,100,101,108,110,115,121,125,127,130,131,134,136,145,147,148,149,150,155,157,159,164,166,167,168,170,173,175,178,181,182,184,185,186,189,193,194,195,196,197,200,203,204,205,210,213,214,215,216,217,218,219,220,224,225,229,230,231,232,233,235,240,241,245,246,247,254,259,260,261,266,267,268,271,277,279,281,285,286,287,290,291,292,293,295,296,299,1,2,4,5,7,10,11,12,13,15,17,22,25,26,30,32,33,34,35,36,39,40,44,45,46,47,49,50,52,53,54,55,56,57,60,61,62,63,67,69,70,72,77],
254))