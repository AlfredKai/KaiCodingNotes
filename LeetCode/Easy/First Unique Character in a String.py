# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        record = {}
        for c in s:
            record[c] = 0 if c not in record else 1
        r = -1
        for i in range(0, len(s)):
            if record[s[i]] == 0:
                r = i
                break
        return r

a = Solution()
print(a.firstUniqChar("leetcode"))
print(a.firstUniqChar("loveleetcode"))