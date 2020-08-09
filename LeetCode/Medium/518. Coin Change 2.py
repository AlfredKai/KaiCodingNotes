from typing import List
from collections import defaultdict

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0
        count = {}

        for c in coins:
            temp = c
            newCount = count.copy()
            while temp <= amount:
                for n in count:
                    if n + temp > amount:
                        break
                    if n != 0 and count[n] > 0:
                        if n+temp not in newCount:
                            newCount[n + temp] = 1
                        else:
                            newCount[n + temp] += count[n]
                if temp not in newCount:
                    newCount[temp] = 1
                else:
                    newCount[temp] += 1
                temp += c
            count = newCount
        return count[amount]

a = Solution()
# print(a.change(5, [1, 2, 5]))
# print(a.change(500, [1, 2, 5]))
print(a.change(50, [2,7]))
# print(a.change(50, [1,2,5]))
# print(a.change(50, [1,2,5]))