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

        # Solution 1 - Using recursive DFS
        # https://www.youtube.com/watch?v=lla6QlAF4HQ&t=184s
        # Time - O(m * n)
        # Space - O(m * n)

        # x, y = click

        # if not (0 <= x < len(board) and 0 <= y < len(board[0])):
        #     return None

        # if board[x][y] == "M":
        #     board[x][y] = 'X'
        #     return board
        # elif board[x][y] == "E":
        #     mines = self.get_adjacent_mines(board, x, y)

        #     if mines:
        #         board[x][y] = str(mines)
        #     else:
        #         board[x][y] = 'B'
        #         for r in range(x - 1, x + 2):
        #             for c in range(y - 1, y + 2):
        #                 self.updateBoard(board, [r, c])

        # return board


        # Solution 2 - BFS using queue
        # https://www.youtube.com/watch?v=lla6QlAF4HQ&t=184s
        # Time - O(m*n)
        # Space - O(m*n)

        if not board:
            return board

        ROWS, COLS = len(board), len(board[0])
        q = collections.deque()
        q.append(click)

        while q:
            x, y = q.popleft()

            if board[x][y] == "M":
                board[x][y] = "X"
                return board
            elif board[x][y] == "E":
                mines = 0

                for r in range(x - 1, x + 2):
                    for c in range(y - 1, y + 2):
                        if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "M":
                            mines += 1
                
                if mines:
                    board[x][y] = str(mines)
                else:
                    board[x][y] = "B"

                    for r in range(x - 1, x + 2):
                        for c in range(y - 1, y + 2):
                            if 0 <= r < ROWS and 0 <= c < COLS:
                                q.append((r, c))

        return board