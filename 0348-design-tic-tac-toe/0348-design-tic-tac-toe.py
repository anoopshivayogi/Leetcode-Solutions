class TicTacToe:

    def __init__(self, n: int):
        # self.n = n
        # self.rows = [0] * n
        # self.cols = [0] * n
        # self.diagonal = 0
        # self.antidiagonal = 0

        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:

        # if player == 1:
        #     self.rows[row] += 1
        #     if self.rows[row] == self.n:
        #         return 1

        #     self.cols[col] += 1
        #     if self.cols[col] == self.n:
        #         return 1

        #     if row == col:
        #         self.diagonal += 1
        #         if self.diagonal == self.n:
        #             return 1

        #     if row+col == self.n-1:
        #         self.antidiagonal += 1
        #         if self.antidiagonal == self.n:
        #             return 1

        # else:

        #     self.rows[row] -= 1
        #     if self.rows[row] == -self.n:
        #         return 2

        #     self.cols[col] -= 1
        #     if self.cols[col] == -self.n:
        #         return 2

        #     if row == col:
        #         self.diagonal -= 1
        #         if self.diagonal == -self.n:
        #             return 2

        #     if row+col == self.n-1:
        #         self.antidiagonal -= 1
        #         if self.antidiagonal == -self.n:
        #             return 2

        # return 0

        cur_player = 1
        if player == 2:
            cur_player = -1


        # Row match
        self.rows[row] += cur_player
        if self.rows[row] == self.n or self.rows[row] == -self.n:
            return player

        # Column match
        self.cols[col] += cur_player
        if self.cols[col] == self.n or self.cols[col] == -self.n:
            return player


        # Diagonal match
        if row == col:
            self.diagonal += cur_player
            if self.diagonal == self.n or self.diagonal == -self.n:
                return player

        # Anti-diagonal match
        if row + col == self.n - 1:
            self.anti_diagonal += cur_player
            if self.anti_diagonal == self.n or self.anti_diagonal == -self.n:
                return player

        return 0

    #       0  1. 2
    #   0  [0, 0, 0]
    #   1  [0, 0, 0]
    #   2  [0, 0, 0]


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)