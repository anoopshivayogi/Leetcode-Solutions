class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Solution 1 - using DFS with visit set. 
        # Time - O(m*n)
        # Space - O(m*n) 

        # visit = set()
        # ROWS, COLS = len(board), len(board[0])

        # directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # def dfs(r, c):
        #     visit.add((r, c))
            
        #     for d in directions:
        #         new_r, new_c = d[0] + r, d[1] + c

        #         if new_r >= 0 and new_r < ROWS and new_c >=0 \
        #             and new_c < COLS and (new_r, new_c) not in visit and board[new_r][new_c] == 'X':
        #             dfs(new_r, new_c)

        # res = 0

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if (r, c) not in visit and board[r][c] == 'X':
        #             dfs(r, c)
        #             res += 1

        # return res


        # Solution 2 - 
        # Time - O(m*n)
        # Space - O(1)

        res = 0

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):

                prev_r, prev_c = r-1, c-1

                if (prev_r < 0 or board[prev_r][c] == '.') and (prev_c < 0 or board[r][prev_c] == '.') and board[r][c] == 'X':
                    res += 1

        return res
        