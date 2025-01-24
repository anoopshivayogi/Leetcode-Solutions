class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        # Solution 1 - Using rows and cols number of variables
        # Time - O((m * n) + m + n)
        # Space - O(m * n)


        # if not grid:
        #     return 0

        # ROWS, COLS = len(grid), len(grid[0])
        # row_seen, col_seen = [set() for _ in range(ROWS)], [set() for _ in range(COLS)]

        # for r in range(ROWS):
        #     for c in range(COLS):

        #         if grid[r][c]:
        #             row_seen[r].add((r, c))
        #             col_seen[c].add((r, c))

        # res = set()

        # for r in range(ROWS):
        #     if len(row_seen[r]) > 1:
        #         for ele in row_seen[r]:
        #             res.add(ele)

        # for c in range(COLS):
        #     if len(col_seen[c]) > 1:
        #         for ele in col_seen[c]:
        #             res.add(ele)

        # return len(res)


        # Solution 2 - Using just rows and cols counter
        # Time - O(m * n)
        # Space - O(m + n)

        ROWS, COLS = len(grid), len(grid[0])
        row_count, col_count = [0] * ROWS, [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    row_count[r] += 1
                    col_count[c] += 1
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    if row_count[r] > 1 or col_count[c] > 1:
                        res += 1

        return res