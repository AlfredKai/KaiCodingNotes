class Solution:
    def isPalindrome(self, s: str) -> bool:
        rightIndex = len(s)
        for i in range(0, len(s)):
            if s[i].isalnum():
                if rightIndex - i == 1 or rightIndex == i:
                    return True
                while rightIndex > i:
                    rightIndex -= 1
                    if s[rightIndex].isalnum():
                        if s[i].lower() == s[rightIndex].lower():
                            break
                        else:
                            return False
                else:
                    return True
        else:
            return True



a = Solution()
print(a.isPalindrome('A man, a plan, a canal: Panama'))
print(a.isPalindrome('race a car'))
print(a.isPalindrome(''))
print(a.isPalindrome(' '))
print(a.isPalindrome('aa'))
print(a.isPalindrome('OP'))
print(a.isPalindrome('0P'))
print(a.isPalindrome('ab@a'))