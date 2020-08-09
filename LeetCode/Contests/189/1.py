from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        st = []
        for i, s in enumerate(startTime):
            if s <= queryTime:
                st.append(i)
        r = 0
        for i in st:
            if endTime[i] >= queryTime:
                r += 1
        return r