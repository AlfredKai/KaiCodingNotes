from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return nums
        nums = [(n, i) for i, n in enumerate(nums)]
        result = [0] * len(nums)
        def merge(nums, l, mid, r):
            i = l
            j = mid + 1
            temp = []
            while i <= mid and j <= r:
                if nums[i][0] <= nums[j][0]:
                    temp.append(nums[i])
                    result[nums[i][1]] += j - mid - 1
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                result[nums[i][1]] += j - mid - 1
                i += 1
            while j <= mid:
                temp.append(nums[j])
                j += 1
            for i, n in enumerate(temp):
                nums[l+i] = n

        def mergesort(nums, l, r):
            if r == l:
                return nums[l]

            mid = (r+l) // 2
            mergesort(nums, l, mid)
            mergesort(nums, mid+1, r)
            merge(nums, l, mid, r)

        mergesort(nums, 0, len(nums)-1)

        return result

a = Solution()
# print(a.countSmaller([5,2,6,1]))
# print(a.countSmaller([-1,-1]))
print(a.countSmaller([-1,-1,-1,-1]))
# print(b)