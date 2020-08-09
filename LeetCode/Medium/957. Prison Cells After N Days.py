from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if not cells:
            return []

        cell_history = {str(cells[0]): 0}
        cell_history_rec = [cells]
        
        for i in range(N):
            next_cells = [0] * len(cells)
            for j in range(1, len(cells)-1):
                next_cells[j] = 1 if cells[j-1] == cells[j+1] else 0
            if str(next_cells) in cell_history:
                index = cell_history[str(next_cells)]
                loop = i - index
                r = (N - (index + 1)) % loop + (index + 1)
                return cell_history_rec[r]
            # print(next_cells)
            cell_history_rec.append(next_cells)
            cell_history[str(next_cells)] = i
            cells = next_cells
        return cells

a = Solution()
print(a.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))