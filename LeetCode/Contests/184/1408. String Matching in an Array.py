from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                found = False
                if len(words[i]) < len(words[j]):
                    lastIndex = len(words[j]) - len(words[i]) + 1
                    for k in range(lastIndex):
                        if words[i] == words[j][k:k + len(words[i])]:
                            result.append(words[i])
                            found = True
                            break
                if found:
                    break
        return result

a = Solution()
print(a.stringMatching(["mass","as","hero","superhero"]))
print(a.stringMatching(["leetcoder","leetcode","od","hamlet","am"]))