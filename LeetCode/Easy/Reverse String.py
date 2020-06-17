import math
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, math.ceil(len(s)/2)):
            temp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = temp
        return s

a = Solution()
b = ["h","e","l","l","o"]
a.reverseString(b)
print(b)
a = Solution()
b = ["H","a","n","n","a","h"]
a.reverseString(b)
print(b)

# recursion version

class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            return s
        if len(s) == 0:
            return s
        s = [s[-1]] + self.reverseString(s[1:-1]) + [s[0]]
        print(s)
        return s

a = Solution2()
b = ["h","e","l","l","o"]
a.reverseString(b)
print(b)
a = Solution2()
b = ["H","a","n","n","a","h"]
a.reverseString(b)
print(b)