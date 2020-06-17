from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberLetterMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        if len(digits) == 1:
            return numberLetterMap[digits[0]]

        preResult = self.letterCombinations(digits[:-1])
        result = []
        for d in numberLetterMap[digits[-1]]:
            result.extend(
                list(map(lambda x: x + d, preResult))
            )
        return result

class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return ''

        numberLetterMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        curResult = numberLetterMap[digits[0]]
        if len(digits) == 1:
            return curResult

        for d in digits[1:]:
            result = []
            for l in numberLetterMap[d]:
                result.extend(list(map(lambda x: x + l, curResult)))
            curResult = result
        return result

a = Solution2()
print(a.letterCombinations('235'))