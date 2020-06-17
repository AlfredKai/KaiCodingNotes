from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        r = [0] * (num + 1)
        r[1] = 1
        p2 = 2
        for i in range(2, num + 1):
            lookback = p2 // 2
            if i % p2 < lookback:
                r[i] = r[i-lookback]
            else:
                r[i] = r[i-lookback] + 1
            if i+1 == p2 * 2:
                p2 *= 2
        return r

a = Solution()
a.countBits(10)