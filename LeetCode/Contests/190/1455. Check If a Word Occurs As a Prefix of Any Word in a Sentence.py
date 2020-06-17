class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sp = sentence.split(' ')
        for i, word in enumerate(sp):
            if len(word) < len(searchWord):
                continue
            for j, c in enumerate(searchWord):
                if c != word[j]:
                    break
            else:
                return i + 1
        return -1

a = Solution()
print(a.isPrefixOfWord("i love eating burger", "burg"))