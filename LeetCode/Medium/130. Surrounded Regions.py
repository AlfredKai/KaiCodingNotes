class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        keepOs = set()

        def DFS(v, block):
            if v == 'X':
                return
            if block not in keepOs:
                keepOs.add(block)
                x, y = block
                if x-1 > 0:
                    DFS(board[x-1][y], (x-1, y))
                if x+1 < len(board):
                    DFS(board[x+1][y], (x+1, y))
                if y-1 > 0:
                    DFS(board[x][y-1], (x, y-1))
                if y+1 < len(board[0]):
                    DFS(board[x][y+1], (x, y+1))

        for i in range(len(board)):
            DFS(board[i][0], (i, 0))
            DFS(board[i][len(board[0])-1], (i, len(board[0])-1))

        for i in range(len(board[0])):
            DFS(board[0][i], (0, i))
            DFS(board[len(board)-1][i], (len(board)-1, i))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in keepOs:
                    board[i][j] = 'X'