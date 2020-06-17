from typing import List

class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {}
        for edge in prerequisites:
            if edge[0] in d:
                d[edge[0]].append(edge[1])
            else:
                d[edge[0]] = [edge[1]]
        r = set([i for i in range(numCourses)])
        while len(r) > 0:
            checked = set()
            for i in d:
                for j in d[i]:
                    checked.add(j)
            diff = r - checked
            if len(diff) == 0:
                return False
            for k in r - checked:
                if k in d:
                    del d[k]
            r = checked
        return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}
        for edge in prerequisites:
            if edge[0] in adj_list:
                adj_list[edge[0]].append(edge[1])
            else:
                adj_list[edge[0]] = [edge[1]]

        inDegreed = dict([(i, 0) for i in range(numCourses)])
        for edge in prerequisites:
            if edge[1] in inDegreed:
                inDegreed[edge[1]] += 1
            else:
                inDegreed[edge[1]] = 1
        zeroDegree = []
        for deg in inDegreed:
            if inDegreed[deg] == 0:
                zeroDegree.append(deg)
        count = 0
        while zeroDegree:
            zeroDegreePoint = zeroDegree.pop()
            count += 1
            if zeroDegreePoint in adj_list:
                for e in adj_list[zeroDegreePoint]:
                    inDegreed[e] -= 1
                    if inDegreed[e] == 0:
                        zeroDegree.append(e)
        return count == numCourses

a = Solution()
# print(a.canFinish(2, [[1,0],[0,1]]))
# print(a.canFinish(2, [[1,0]]))
print(a.canFinish(3, [[1,0]]))
# print(a.canFinish(1, []))