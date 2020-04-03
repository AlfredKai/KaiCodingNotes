from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            last = nums[-1]
            for j in range(len(nums) - 1, 0, -1):
                nums[j] = nums[j - 1]
            else:
                nums[0] = last

a = Solution()
b = [1,2,3,4,5,6,7]
a.rotate(b, 3)
print(b)
b = [-1,-100,3,99]
a.rotate(b, 2)
print(b)

class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        length = len(nums)
        a = nums + nums
        b = a[length - k: length - k + length]
        for i in range(0, len(nums)):
            nums[i] = b[i]

a = Solution2()
b = [1,2,3,4,5,6,7]
a.rotate(b, 3)
print(b)
b = [-1,-100,3,99]
a.rotate(b, 2)
print(b)