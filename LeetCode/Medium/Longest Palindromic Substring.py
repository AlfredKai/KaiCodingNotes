class Solution:
    def longestPalindrome(self, s: str) -> str:
        mem = set()
        result = ''
        for l in range(1, len(s) + 1):
            for i in range(0, len(s) - l + 1):
                if l == 1:
                    if s[i] not in mem:
                        mem.add(s[i])
                        if len(s[i]) > len(result):
                            result = s[i]
                    continue
                if l == 2: 
                    if s[i:i+2] not in mem and s[i] == s[i+1]:
                        mem.add(s[i:i+2])
                        if len(s[i:i+2]) > len(result):
                            result = s[i:i+2]
                    continue
                # print(s[i:i+l], s[i+1:i+l-1], s[i], s[i+l-1])
                if s[i] == s[i+l-1] and s[i:i+l] not in mem and s[i+1:i+l-1] in mem:
                    mem.add(s[i:i+l])
                    if len(s[i:i+l]) > len(result):
                        result = s[i:i+l]

        # result = ''
        # # print(mem)
        # for e in mem:
        #     if len(e) > len(result):
        #         result = e
        return  result

a = Solution()
print(a.longestPalindrome('abccbe'))