from typing import List

def mergesort(nums: List):
    if len(nums) == 1:
        return [nums[0]]

    l = mergesort(nums[0:len(nums)//2])
    r = mergesort(nums[len(nums)//2:len(nums)])
    ret = []
    i = j = 0
    while i < len(l) or j < len(r):
        if j == len(r) and i < len(l):
            ret.append(l[i])
            i+=1
            continue
        if i == len(l) and j < len(r):
            ret.append(r[j])
            j+=1
            continue
        if l[i] < r[j]:
            ret.append(l[i])
            i+=1
        else:
            ret.append(r[j])
            j+=1
    return ret

print(mergesort([3,2,6,1,5]))