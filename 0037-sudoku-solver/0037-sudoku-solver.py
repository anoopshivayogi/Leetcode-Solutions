class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        


        # Solution 1 - Using backtracking 
        # Time - (9!)^9 -> 9! is coming from each row and there are 9 rows
        # Space - O(1)

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grids = collections.defaultdict(set)

        ROWS, COLS = 9, 9

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != ".":
                    num = int(board[r][c])
                    rows[r].add(num)
                    cols[c].add(num)
                    grids[(r // 3, c // 3)].add(num)

        def dfs(r, c):

            if r == 9:
                return True

            new_c = (c + 1) % 9  # Cycle through 0 -> 8
            new_r = r + (c + 1) // 9   # Add 1 when the column reaches value = 9

            if board[r][c] != ".":
                if dfs(new_r, new_c):
                    return True
            else:
                for num in range(1, 10):
                    if num not in rows[r] and num not in cols[c] and num not in grids[(r // 3, c // 3)]:
                        rows[r].add(num)
                        cols[c].add(num)
                        grids[(r // 3, c // 3)].add(num)
                        board[r][c] = str(num)
                        if dfs(new_r, new_c):
                            return True
                        rows[r].remove(num)
                        cols[c].remove(num)
                        grids[(r // 3, c // 3)].remove(num)
                        board[r][c] = "."

            return False

        dfs(0, 0)
