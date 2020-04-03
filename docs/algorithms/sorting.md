# Sorting

## Merge Sort

### GeeksForGeeks

```py
# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves
  
        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half
  
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
  
# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
  
# This code is contributed by Mayank Khanna
```

### jwasham

```py
class MergeSort(object):
    def __init__(self, numbers):
        self.values = numbers
        self.count = len(numbers)

    def sort(self):
        self.merge_sort(0, self.count - 1)
        return self.values

    def merge_sort(self, low, high):
        if low < high:
            mid = (low + high) // 2

            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)

    def merge(self, low, mid, high):
        b = []
        i = low
        j = mid + 1

        while i <= mid and j <= high:
            if self.values[i] <= self.values[j]:
                b.append(self.values[i])
                i += 1
            else:
                b.append(self.values[j])
                j += 1

        while i <= mid:
            b.append(self.values[i])
            i += 1

        while j <= high:
            b.append(self.values[j])
            j += 1

        for index, val in enumerate(b):
            self.values[low + index] = val
```

### me

```py
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
```
