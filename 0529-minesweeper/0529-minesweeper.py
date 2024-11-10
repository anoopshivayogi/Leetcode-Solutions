class Solution:

    def get_adjacent_mines(self, board, x, y):
        num = 0

        for r in range(x - 1, x + 2):
            for c in range(y - 1, y + 2):
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    if board[r][c] == 'M':
                        num += 1

        return num


    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        #       0   1.  2.  3.  4
        # 0  [["E","E","E","E","E"], 
        # 1   ["E","E","M","E","E"],
        # 2   ["E","E","E","E","E"],
        # 3   ["E","E","E","E","E"]]
            
        #.   click = [3,0]

        x, y = click

        if not (0 <= x < len(board) and 0 <= y < len(board[0])):
            return None

        if board[x][y] == "M":
            board[x][y] = 'X'
            return board
        elif board[x][y] == "E":
            mines = self.get_adjacent_mines(board, x, y)

            if mines:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for r in range(x - 1, x + 2):
                    for c in range(y - 1, y + 2):
                        self.updateBoard(board, [r, c])

        return board