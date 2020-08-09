from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        comSets = {}
        for p, coms in enumerate(favoriteCompanies):
            for c in coms:
                if c not in comSets:
                    comSets[c] = set()
                comSets[c].add(p)
        r = []
        for p, coms in enumerate(favoriteCompanies):
            selfSet = set()
            selfSet.add(p)
            itc = comSets[coms[0]] - selfSet
            if len(itc) == 0:
                r.append(p)
                continue
            for i in range(1, len(coms)):
                itc = itc.intersection(comSets[coms[i]] - selfSet)
                if len(itc) == 0:
                    r.append(p)
                    break
        return r


a = Solution()
print(a.peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))