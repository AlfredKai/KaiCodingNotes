from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        r = []
        for i in range(1, n + 1):
            t = str(i)
            if i % 15 == 0:
                t = 'FizzBuzz'
            elif i % 3 == 0:
                t = 'Fizz'
            elif i % 5 == 0:
                t = 'Buzz'
            r.append(t)
        return r

a = Solution()
print(a.fizzBuzz(15))