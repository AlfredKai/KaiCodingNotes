class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for c in s:
            if c in '([{':
                a.append(c)
            elif c == ']':
                if len(a) == 0 or a.pop() != '[':
                    return False
            elif c == '}':
                if len(a) == 0 or a.pop() != '{':
                    return False
            elif c == ')':
                if len(a) == 0 or a.pop() != '(':
                    return False
        return len(a) == 0