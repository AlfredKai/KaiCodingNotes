class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        maxV = 0
        for i in range(k):
            if s[i] in vowels:
                maxV += 1
        i = 1
        j = k
        cur = maxV
        while j < len(s):
            if s[i-1] in vowels:
                cur -= 1
            if s[j] in vowels:
                cur += 1
            if cur > maxV:
                maxV = cur
            i += 1
            j += 1
        return maxV

a = Solution()
print(a.maxVowels("weallloveyou",7))
print(a.maxVowels("novowels", 1))