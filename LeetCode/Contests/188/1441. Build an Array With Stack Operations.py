from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        fillOp = ["Push", "Pop"]
        a = []
        start = 0
        for n in target:
            gap = n - start - 1
            start = n
            for i in range(gap):
                a.extend(fillOp)
            a.append("Push")
        return a

a = Solution()
# print(a.buildArray([1,3],3))
print(a.buildArray([2,3,4],4))