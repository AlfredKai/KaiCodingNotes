class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croakSeq = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        frogs = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, -1: 0}
        for c in croakOfFrogs:
            if c not in croakSeq:
                return -1
            if frogs[croakSeq[c]-1] > 0:
                if croakSeq[c] == 4:
                    frogs[-1] += 1
                else:
                    frogs[croakSeq[c]] += 1
                frogs[croakSeq[c]-1] -= 1
            else:
                if c == 'c':
                    frogs[0] += 1
        for k in frogs:
            if k == -1:
                continue
            if frogs[k] != 0:
                return -1
        return frogs[-1]

    # time limit exceeded
    def minNumberOfFrogs1(self, croakOfFrogs: str) -> int:
        croakSeq = ['c', 'r', 'o', 'a', 'k']
        frogQue = []
        for c in croakOfFrogs:
            if c not in croakSeq:
                return -1
            for i in range(len(frogQue)):
                # print(frogQue)
                if frogQue[i] + 1 == croakSeq.index(c):
                    frogQue[i] = croakSeq.index(
                        c) if croakSeq.index(c) < 4 else -1
                    break
            else:
                if c == croakSeq[0]:
                    frogQue.append(0)
                else:
                    return -1
        for f in frogQue:
            if f != -1:
                return -1
        return len(frogQue)

    # time limit exceeded
    def minNumberOfFrogs2(self, croakOfFrogs: str) -> int:
        croakPos = set()
        croakSeq = ['c', 'r', 'o', 'a', 'k']
        r = 0
        pivot = 0
        while len(croakOfFrogs) > 0:
            temp = set()
            for i in range(len(croakOfFrogs)):
                if croakOfFrogs[i] == croakSeq[pivot]:
                    temp.add(i)
                    if pivot < 4:
                        pivot += 1
                    else:
                        croakPos |= temp
                        pivot = 0
            if len(croakPos) == 0:
                return -1
            new = []
            for i in range(len(croakOfFrogs)):
                if i not in croakPos:
                    new.append(croakOfFrogs[i])
            croakPos.clear()
            croakOfFrogs = new
            r += 1
        return r


a = Solution()
print(a.minNumberOfFrogs('croakcroak'))
print(a.minNumberOfFrogs('crcoakroak'))
print(a.minNumberOfFrogs('leetcroad'))
print(a.minNumberOfFrogs('croakcrook'))
print(a.minNumberOfFrogs('croakcroa'))
