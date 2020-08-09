class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            longer = a
            shorter = b
        else:
            longer = b
            shorter = a
        carry = 0
        r = ''
        for a_digit, b_digit in zip(reversed(a), reversed(b)):
            if a_digit == '1' and b_digit == '1':
                if carry:
                    r = '1' + r
                else:
                    r = '0' + r
                carry = 1
            elif a_digit == '0' and b_digit == '0':c
                if carry:
                    r = '1' + r
                else:
                    r = '0' + r
                carry = 0
            else:
                if carry:
                    r = '0' + r
                    carry = 1
                else:
                    r = '1' + r
                    carry = 0
        for i in reversed(range(len(longer) - len(shorter))):
            if longer[i] == '1':
                if carry:
                    r = '0' + r
                    carry = 1
                else:
                    r = '1' + r
                    carry = 0
            else:
                if carry:
                    r = '1' + r
                else:
                    r = '0' + r
                carry = 0
        if carry:
            r = '1' + r
        return r

a = Solution()
print(a.addBinary('1010', '1011'))