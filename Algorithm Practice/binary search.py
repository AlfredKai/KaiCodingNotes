def binarySearch(arr, l, r, x):
    while l <= r:
        mid = (r + l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r =  mid - 1
        else:
            l = mid + 1
    return -1

a = [1, 2, 4, 4, 8]
print(binarySearch([1, 2, 4, 4, 8], 0, len(a) - 1 ,8))