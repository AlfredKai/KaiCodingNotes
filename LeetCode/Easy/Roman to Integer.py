class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        r = 0
        skipFlag = False
        for i in range(0, len(s)):
            if skipFlag:
                skipFlag = False
                continue
            if i != len(s) - 1 and map[s[i]] < map[s[i+1]]:
                r += map[s[i+1]] - map[s[i]]
                skipFlag = True
            else:
                r += map[s[i]]
        return r

a = Solution()
print(a.romanToInt("III"))
print(a.romanToInt("IV"))
print(a.romanToInt("IX"))
print(a.romanToInt("LVIII"))
print(a.romanToInt("MCMXCIV"))