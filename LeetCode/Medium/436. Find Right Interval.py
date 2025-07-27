from typing import List

class Interval:
    def __init__(self, type, val, index):
        self.type = type
        self.val = val
        self.index = index

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        itls = []
        for i, interval in enumerate(intervals):
            itls.append(Interval('start', interval[0], i))
            itls.append(Interval('end', interval[1], i))
        itls.sort(key=lambda x: x.val)
        r = [-1] * len(intervals)
        current_end = []
        cur_val = itls[0].val
        start_itl = None
        for itl in itls:
            if itl.val != cur_val and start_itl:
                while current_end:
                    end = current_end.pop()
                    r[end.index] = start_itl.index
                start_itl = None
                cur_val = itl.val
            if itl.type == 'end':
                current_end.append(itl)
            if itl.type == 'start':
                start_itl = itl
                while current_end:
                    end = current_end.pop()
                    r[end.index] = itl.index
        return r