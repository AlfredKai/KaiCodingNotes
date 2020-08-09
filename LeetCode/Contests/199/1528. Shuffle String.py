from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r = ['' for i in range(len(indices))]

        for i in indices:
            r[indices[i]] = s[i]
        
        return ''.join(r)