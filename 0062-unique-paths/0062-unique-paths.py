from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Approach 1 - Top Down with memoization

        # cache = {}
        
        # @lru_cache
        # def top_down(i, j):
        #     # if (i, j) in cache:
        #     #     return cache[(i, j)]

        #     if i == 0 or j == 0:
        #         return 0
            
        #     if i == 1 and j == 1:
        #         return 1

        #     res = top_down(i-1, j) + top_down(i, j-1)

        #     # cache[(i, j)] = res
        #     return res

        
        # return top_down(m, n)


        # # Approach 2 - Bottom Up solution with tabulation

        # table = [[0] * n for i in range(m)]
        # table[0][0] = 1

        # def top_down(r, c):
            
        #     for i in range(r):
        #         for j in range(c):
        #             if i-1 >= 0:
        #                 table[i][j] += table[i-1][j]
        #             if j-1 >= 0:
        #                 table[i][j] += table[i][j-1]

        #     return table[r-1][c-1]

        # return top_down(m, n)

            
            
        # cache = {}

        # def number_of_paths(r, c):
        #     if (r, c) in cache:
        #         return cache[(r, c)]

        #     if r == m-1 and c == n-1:
        #         return 1

        #     if r >= m or c >= n:
        #         return 0

        #     right = number_of_paths(r, c+1)
        #     down = number_of_paths(r+1, c)

        #     res = right + down
        #     cache[(r, c)] = res

        #     return res

        # return number_of_paths(0, 0)


        # Re-do for the interview

        # Time - O(2*m*n)
        # Space - O(2*m*n)

        from functools import cache

        @cache
        def dfs(i, j):
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)
