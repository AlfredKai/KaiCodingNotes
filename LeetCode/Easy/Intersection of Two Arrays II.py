from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1Dic = {}
        for num in nums1:
            if num not in nums1Dic:
                nums1Dic[num] = 1
            else:
                nums1Dic[num] += 1

        for num in nums2:
            if num in nums1Dic and nums1Dic[num] > 0:
                result.append(num)
                nums1Dic[num] -= 1

        return result

a = Solution()
print(a.intersect([1,2,2,1], [2,2]))
print(a.intersect([4,9,5], [9,4,9,8,4]))
