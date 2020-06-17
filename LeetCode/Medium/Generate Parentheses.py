from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r = []
        if n == 0:
            return r
        def helper(left, right, temp):
            print(left, right, temp)
            if left == 0 and right == 0:
                r.append(temp)
                return
            if left < right:
                if left > 0:
                    helper(left - 1, right, temp + '(')
                if right > 0:
                    helper(left, right - 1, temp + ')')
            else:
                if left > 0:
                    helper(left - 1, right, temp + '(')
        helper(n, n, '')
        return r

a = Solution()
print(a.generateParenthesis(4))