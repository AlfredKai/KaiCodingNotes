from typing import List

class Solution2:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j, len(arr)):
                    a = 0
                    b = 0
                    for ai in range(i, j):
                        a ^= arr[ai]
                    for bi in range(j, k+1):
                        b ^= arr[bi]
                    if a == b:
                        count += 1
        return count

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cum = [0]
        for n in arr:
            cum.append(cum[-1]^n)
        ans=0
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                xorAll = cum[j+1] ^ cum[i]
                if xorAll == 0:
                    ans += j - i
        return ans

        

a = Solution()
print(a.countTriplets([2,3,1,6,7]))                   