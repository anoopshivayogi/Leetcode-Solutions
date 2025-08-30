from collections import defaultdict 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # r_dict, c_dict, sb_dict = defaultdict(set), defaultdict(set), defaultdict(set)

        # for r in range(len(board[0])):
        #     for c in range(len(board)):
        #         if board[r][c] == '.':
        #             continue
        #         if (board[r][c] in r_dict[r]) or (board[r][c] in c_dict[c]) or (board[r][c] in sb_dict[(r//3, c//3)]):
        #             return False
        #         r_dict[r].add(board[r][c])
        #         c_dict[c].add(board[r][c])
        #         sb_dict[(r//3, c//3)].add(board[r][c])

        # return True



        # Re-Do for the interview
        # Time - O(N^2)
        # Space - O(N^2)

        from collections import defaultdict


        row_set, col_set, grid_set = defaultdict(set), defaultdict(set), defaultdict(set)
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in row_set[r]) or (board[r][c] in col_set[c]) or (board[r][c] in grid_set[(r // 3, c // 3)]):
                    return False


                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                grid_set[(r // 3, c // 3)].add(board[r][c])

        return True
