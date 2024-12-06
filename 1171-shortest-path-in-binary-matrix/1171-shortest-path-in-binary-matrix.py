class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # solution 1 - BFS solution
        # Time - O(m*n); if all the cells were zero; it will go to every cell
        # Space - O(m*n); same as the above, queue will be enqued with at most m*n cells

        # ROWS, COLS = len(grid), len(grid[0])

        # # Addressing edge cases; if the starting path is -1 or ending path is -1 then solution is not possible 

        # if grid[0][0] or grid[-1][-1]:
        #     return -1

        # directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        # from collections import deque

        # q = deque([(0, 0, 1)])
        # grid[0][0] = 1

        # while q:
        #     r, c, path_len = q.popleft()

        #     if r == ROWS - 1 and c == COLS - 1:
        #         return path_len

        #     for r_inc, c_inc in directions:
        #         new_r, new_c = r + r_inc, c + c_inc

        #         if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 0:
        #             grid[new_r][new_c] = 1  # Make it 1 so that we do not visit again; otherwise use visit set()
        #             q.append((new_r, new_c, path_len + 1))

        # return -1


        # Re-do for the interview
        # Time - O(m*n)
        # Space - O(m*n)

     

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:   # NOTE: VERY VERY IMP
            return -1

        q = collections.deque()
        q.append((0, 0, 1)) # row, col, path
        visit = set()
        # grid[0][0] = 1
        visit.add((0, 0))

        def bfs():

            while q:
                cur_r, cur_c, path = q.popleft()

                if cur_r == ROWS - 1 and cur_c == COLS - 1:
                    return path

                for inc_r, inc_c in directions:
                    new_r, new_c = cur_r + inc_r, cur_c + inc_c

                    if (new_r, new_c) not in visit and 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 0:
                        # grid[new_r][new_c] = 1
                        visit.add((new_r, new_c))
                        q.append((new_r, new_c, path + 1))

            return -1 # NOTE: IMPP!!!


        return bfs()
