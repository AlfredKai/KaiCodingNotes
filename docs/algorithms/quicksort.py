from typing import List

def quicksort(nums: List):
    # if len(nums) == 1:
    #     return [nums[0]]
    # if len(nums) == 0:
    #     return []
    if not nums:
        return nums
    pivot = nums[-1]
    l = []
    r = []
    for i in range(0, len(nums) - 1):
        if nums[i] < pivot:
            l.append(nums[i])
        else:
            r.append(nums[i])
    return quicksort(l) + [pivot] + quicksort(r)

print(quicksort([3,2,6,7,4,2]))