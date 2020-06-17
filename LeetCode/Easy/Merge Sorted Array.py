from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = [1,2,3,0,0,0], m = 3
        # nums2 = [2,5,6],       n = 3
        i = 0
        for num2 in nums2:
            n -= 1
            while i <= m - 1:
                if nums1[i] < num2:
                    i += 1
                else:
                    for j in range(m, i, -1):
                        nums1[j] = nums1[j-1]
                    nums1[i] = num2
                    break
            else:
                nums1[m] = num2
            m += 1

b = [1,2,3,0,0,0]
a = Solution()
a.merge(b, 3, [2,5,6], 3)
print(b)
b = [2, 0]
a.merge(b, 1, [1], 1)
print(b)