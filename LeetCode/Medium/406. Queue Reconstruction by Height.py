from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: x[0])
        newQueue = [[-1,0] for i in range(len(people))]
        for p in people:
            count = 0
            for i, np in enumerate(newQueue):
                if count == p[1] and np[0] == -1:
                    newQueue[i] = p
                    break
                if np[0] == -1 or np[0] == p[0]:
                    count += 1
        return newQueue

a = Solution()
print(a.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))