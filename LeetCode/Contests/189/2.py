class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        startLenghtIndex = [[] for i in range(len(text))]
        start = 0
        for i, t in enumerate(text):
            if t == ' ':
                startLenghtIndex[i - start + 1].append(start)
                start =  i+1
        startLenghtIndex[len(text)-start+1].append(-start)
        r = ''
        for l, sti in enumerate(startLenghtIndex):
            if sti:
                for i in sti:
                    if i < 0:
                        i = -i
                        r += text[i:i+l] + ' '
                    else:
                        r += text[i:i+l]
        return r[0].upper() + r[1:-1]

a = Solution()
print(a.arrangeWords("To be or not to be"))