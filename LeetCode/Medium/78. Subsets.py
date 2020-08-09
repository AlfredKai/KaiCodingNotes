from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = [[]]
        def select(n_set, count):
            l = sorted(list(n_set))
            if l in r:
                return
            r.append(l)
            if count == 1:
                return n_set
            for n in n_set:
                select(n_set - set([n]), count - 1)
        select(set(nums), len(nums))
        return r

a = Solution()
print(a.subsets([1,2,3,4]))