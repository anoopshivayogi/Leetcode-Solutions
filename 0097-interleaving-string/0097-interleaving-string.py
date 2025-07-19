from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # Solution 1 - DFS with memoization 

        # cache = {}
        
        # # @lru_cache(None)
        # def dfs(i, j, k):
        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     if i == len(s1) and j == len(s2) and k == len(s3):
        #         return True

        #     if i < len(s1) and k < len(s3) and s1[i] == s3[k] and dfs(i+1, j, k+1):
        #             return True
        #     if j < len(s2) and k < len(s3) and s2[j] == s3[k] and dfs(i, j+1, k+1):
        #             return True

        #     cache[(i, j)] = False

        #     return False

        # return dfs(0, 0, 0)


        # Solution 2 - Tabulation - bottom up approach.

        # m, n = len(s1), len(s2)

        # if m+n != len(s3):
        #     return False

        # dp = [[False for j in range(n+1)] for i in range(m+1)]

        # dp[m][n] = True

        # for i in range(m, -1, -1):
        #     for j in range(n, -1, -1):
        #         if i < m and dp[i+1][j] and s1[i] == s3[i+j]:
        #             dp[i][j] = dp[i+1][j]
        #         if j < n and dp[i][j+1] and s2[j] == s3[i+j]:
        #             dp[i][j] = dp[i][j+1]
        # return dp[0][0]
            

        from functools import cache

        cache = {}

        # @cache
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]


            if i == len(s1) and j == len(s2) and i + j == len(s3):
                return True

            res = False

            if i < len(s1) and (i+j) < len(s3) and s1[i] == s3[i+j]:
                res = res or dfs(i+1, j)


            if j < len(s2) and (i+j) < len(s3) and s2[j] == s3[i+j]:
                res = res or dfs(i, j+1)


            cache[(i, j)] = res
            

            return res

        return dfs(0, 0)
            


        


            

            

        

        