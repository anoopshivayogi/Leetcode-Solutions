# from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS or DFS both works equally well for this problem

        # if not grid:
        #     return 0

        # visit = set()
        # rows, cols = len(grid), len(grid[0])
        # islands = 0

        # def bfs(r, c):
        #     q = deque()
        #     q.append((r, c))
        #     visit.add((r, c))
        #     directions = [(1,0), (0,1), (-1,0), (0, -1)]

        #     while q:
        #         p = q.popleft()
        #         for i in range(len(directions)):
        #             new_row = p[0] + directions[i][0]
        #             new_col = p[1] + directions[i][1]
        #             if (0 <= new_row < rows) and (0 <= new_col < cols) and ((new_row, new_col) not in visit) and (grid[new_row][new_col] == '1'):
        #                 visit.add((new_row, new_col))
        #                 q.append((new_row, new_col))


        # for r in range(rows):
        #     for c in range(cols):
        #         if (grid[r][c] == '1') and ((r, c) not in visit):
        #             islands += 1
        #             bfs(r, c)

        # return islands





        # BFS Version From Video

        # if not grid:
        #     return 0

        # rows, cols = len(grid), len(grid[0])
        # visited=set()
        # islands=0

        # def bfs(r,c):
        #     q = deque()
        #     visited.add((r,c))
        #     q.append((r,c))

        #     while q:
        #         row,col = q.popleft()
        #         directions= [[1,0],[-1,0],[0,1],[0,-1]]

        #         for dr,dc in directions:
        #             r,c = row + dr, col + dc
        #             if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r ,c) not in visited:

        #                 q.append((r , c ))
        #                 visited.add((r, c ))

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in visited:
        #             bfs(r,c)
        #             islands += 1

        # return islands



        # from collections import deque

        # res = 0
        # visit = set()
        # rows, cols = len(grid), len(grid[0])

        # def bfs(r, c):
        #     directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        #     q = deque()
        #     q.append((r, c))
        #     visit.add((r, c))

        #     while q:
        #         p = q.popleft()

        #         for d in directions:
        #             new_r = p[0] + d[0]
        #             new_c = p[1] + d[1]

        #             if 0 <= new_r < rows and 0 <= new_c < cols and ((new_r, new_c) not in visit) and grid[new_r][new_c] == "1":
        #                 q.append((new_r, new_c))
        #                 visit.add((new_r, new_c))


        # DFS via Recursion 
        # Can also be done using a stack

        # def dfs(r, c):

        #     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        #     for d in directions:
        #         new_r = r + d[0]
        #         new_c = c + d[1]

        #         if  0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visit and grid[new_r][new_c] == "1":
        #             visit.add((new_r, new_c))
        #             dfs(new_r, new_c)


        # for r in range(rows):
        #     for c in range(cols):
        #         if (r, c) not in visit and grid[r][c] == "1":
        #             res += 1
        #             dfs(r, c)

        # return res


        # from collections import deque

        # visit = set()
        # rows, cols = len(grid), len(grid[0])

        # def dfs(r, c):
        #     # q = deque()
        #     # q.append((r, c))
        #     visit.add((r, c))

        #     directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        #     # while q:
        #         # p_row, p_col = q.popleft()

        #     for d in directions:
        #         # new_r, new_c = d[0] + p_row, d[1] + p_col
        #         new_r, new_c = d[0] + r, d[1] + c

        #         if rows > new_r >= 0 and cols > new_c >= 0 and (new_r, new_c) not in visit \
        #             and grid[new_r][new_c] == "1":
        #             # q.append((new_r, new_c))
        #             visit.add((new_r, new_c))
        #             dfs(new_r, new_c)

        # res = 0

        # for r in range(rows):
        #     for c in range(cols):
        #         if (r, c) not in visit and grid[r][c] == "1":
        #             res += 1
        #             dfs(r, c)

        # return res

        # Redo for Google interview

        # BFS and DFS iterative traversal 
        # Time - O(m * n) -- Inplace algorithm
        # Space - O(m * n) 

        ROWS, COLS = len(grid), len(grid[0])
        # visit = set()
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        islands = 0

        def dfs(r, c):

            for inc_r, inc_c in d:
                new_r, new_c = r + inc_r, c + inc_c

                if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == "1":
                    # visit.add((new_r, new_c))
                    grid[new_r][new_c] = '#'
                    dfs(new_r, new_c)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    grid[r][c] = '#'
                    islands += 1
                    dfs(r, c)

        return islands




















                

