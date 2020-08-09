class Solution:
    def minFlips(self, target: str) -> int:
        r = 0
        current_state = '0'
        for state in target:
            if state != current_state:
                current_state = state
                r += 1
        return r