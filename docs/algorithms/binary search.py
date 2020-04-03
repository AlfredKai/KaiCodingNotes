def binarySearch(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r)//2
        if arr[mid] > x:
            r = mid - 1
        elif arr[mid] < x: 
            l = mid + 1
        else:
            return mid
    return -1

def binarySearchRecurrion(arr, x, l, r):
    mid = (l+r) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binarySearchRecurrion(arr, x, l, mid - 1)
    else:
        return binarySearchRecurrion(arr, x, mid + 1, r)
    return -1

a = [1, 2, 4, 4, 8]
print(binarySearch(a ,8))
print(binarySearch(a ,4))
print()
print(binarySearchRecurrion(a ,8, 0, len(a)-1))
print(binarySearchRecurrion(a ,4, 0, len(a)-1))