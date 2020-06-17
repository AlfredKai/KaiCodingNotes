class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        r = ''
        def helper(a,b,c,longest):
            if a == 0 and b == 0 and longest[-2:] == 'ccc' or b == 0 and c == 0 and longest[-2:] == 'aaa' or a == 0 and c == 0 and longest[-2:] == 'bbb':
              return

            nonlocal r
            if len(r) < len(longest):
                r = longest
            if a > 0 and longest[-2:] != 'aa':
                helper(a-1,b,c,longest + 'a')
            if b > 0 and longest[-2:] != 'bb':
                helper(a,b-1,c,longest + 'b')
            if c > 0 and longest[-2:] != 'cc':
                helper(a,b,c-1,longest + 'c')
            return longest

        helper(a,b,c,'')
        return r

a = Solution()
print(a.longestDiverseString(1,1,7))