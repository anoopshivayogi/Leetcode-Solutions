class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])      
        visit = set()  
        res = 0 

        # if not grid:
        #     return 0

        # def dfs(row, col):
        #     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        #     q = collections.deque()
        #     q.append((row, col))
        #     visit.add((row, col))
        #     area = 0

        #     while q:
        #         p_row, p_col = q.popleft()
        #         area += 1
        #         # if col == 8 and row == 3:
        #         #     print('a=', area)
        #         #     print('ele=', (p_row, p_col))
        #         #     print(q)
        #         for d in directions:
        #             n_row = p_row + d[0]
        #             n_col = p_col + d[1]
                
        #             if ((n_row, n_col) not in visit) and (0 <= n_row < ROWS) and (0 <= n_col < COLS) and grid[n_row][n_col] == 1:
        #                 visit.add((n_row, n_col))
        #                 q.append((n_row, n_col))

        #     # if col == 8 and row == 3:
        #     #     print('final', area)

        #     return area
                    
            
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if ((r, c) not in visit) and (grid[r][c] == 1):
        #             res = max(dfs(r, c), res)
        # return res


# Solution 2 -> Recursive solution

        # def dfs(row, col):
        #     print(row, col, ROWS, COLS)
        #     if  row >= ROWS or row < 0 or col >= COLS or col < 0 or ((row, col) in visit) or (grid[row][col] == 0):
        #         return 0

        #     visit.add((row, col))

        #     return 1 + dfs(row+1, col) + dfs(row, col+1) + dfs(row-1, col) + dfs(row, col-1)

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if ((r, c) not in visit) and (grid[r][c] == 1):
        #             res = max(dfs(r, c), res)
        # return res



        # visit = set()
        # res = 0
        # rows, cols = len(grid), len(grid[0])


        # def dfs(r, c):
        #     if rows <= r or r < 0 or cols <= c or c < 0 or (grid[r][c] == 0) or ((r, c) in visit):
        #         return 0

        #     visit.add((r, c))

        #     return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        
        visit = set()
        res = 0
        rows, cols = len(grid), len(grid[0])


        from collections import deque


        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            area = 0
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while q:

                area += 1
                p = q.popleft()

                for d in directions:

                    new_r = p[0] + d[0]
                    new_c = p[1] + d[1]

                    if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visit and grid[new_r][new_c] == 1:
                        visit.add((new_r, new_c))
                        q.append((new_r, new_c))

            return area


        for r in range(rows):
            for c in range(cols):
                if ((r, c) not in visit) and (grid[r][c] == 1):
                    res = max(bfs(r, c), res)

        return res




