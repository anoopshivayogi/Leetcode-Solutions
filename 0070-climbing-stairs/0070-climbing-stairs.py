class Solution:
    def climbStairs(self, n: int) -> int:
    
    # Solution 1 - bottom up approach of solving a DP problem

        # seen = {}

        # def dynamic(i):

        #     if i in seen:
        #         return seen[i]

        #     if i > n:
        #         return 0
            
        #     if i == n:
        #         return 1

        #     steps = dynamic(i+1) + dynamic(i+2)
        #     seen[i] = steps 

        #     return steps
        # return dynamic(0)



    # Solution 2 - up to down approach of solving a DP problem 

        # seen = {}
        # def dynamic(n):

        #     if n in seen:
        #         return seen[n]

        #     if n < 0:
        #         return 0
            
        #     if n == 0:
        #         return 1

        #     steps = dynamic(n-1) + dynamic(n-2)
        #     seen[n] = steps 

        #     return steps

        # return dynamic(n)

    
    # Solution 3 - with just two variables. 


        # one = 1
        # two = 1

        # for i in range(n-1):
        #     temp = one
        #     one = one + two
        #     two = temp

        # return one


    # True DP Solutions 

        # from top to bottom
        # Time - O(n)
        # Time - O(n)

        # dp = [0] * (n+1)
        # dp[0] = 1

        # for i in range(n):
        #     if i + 1 <= n:
        #         dp[i+1] += dp[i]
        #     if i + 2 <= n:
        #         dp[i+2] += dp[i]


        # return dp[n]


        # Solution 2 - from bottom to up
        # Time - O(n)
        # Space - O(n)

        # dp = [0] * (n+1)
        # dp[n] = 1

        # for i in range(n, 0, -1):
        #     if i - 1 >= 0:
        #         dp[i-1] += dp[i]
        #     if i - 2 >= 0:
        #         dp[i-2] += dp[i]

        # return dp[0]



        # Solution - bottom up from left side
        # Time - O(n)
        # Space - O(n)


        # dp = [0] * (n+1)
        # dp[0] = 1

        # for i in range(1, n+1):
        #     if i-1 >= 0:
        #         dp[i] += dp[i-1]
        #     if i-2 >= 0:
        #         dp[i] += dp[i-2]

        # return dp[n]


        # @cache
        # def dfs(i):
        #     if i > n:
        #         return 0

        #     if i == n:
        #         return 1

        #     steps = dfs(i+1) + dfs(i+2)

        #     return steps


        # return dfs(0)


        # @cache
        # def dfs(n):
        #     if n < 0:
        #         return 0

        #     if n == 0:
        #         return 1

        #     steps = dfs(n-1) + dfs(n-2)
        #     return steps


        # return dfs(n)




        # @cache
        # def dfs(i):
        #     if i == n:
        #         return 1

        #     if i > n:
        #         return 0

        #     return dfs(i+1) + dfs(i+2)

        # return dfs(0)


        # Solution x - using 1d array
        # Top Down


        # dp = [0]*(n+1)
        # dp[0] = 1

        # for i in range(n):

        #     if i+1 <= n:
        #         dp[i+1] += dp[i]

        #     if i+2 <= n:
        #         dp[i+2] += dp[i]

        # return dp[n]


        # Solution y - using 1d array
        # Bottom up


        # dp = [0]*(n+1)
        # dp[n] = 1

        # for i in range(n, -1, -1):

        #     if i-1 >= 0:
        #         dp[i-1] += dp[i]

        #     if i-2 >= 0:
        #         dp[i-2] += dp[i]

        # return dp[0]


        # one, two = 1, 1

        # for i in range(n-1):
        #     # temp = two
        #     one = one + two
        #     two = one

        # return two

        # dp = [0] * (n+1)
        # dp[n] = 1

        # for i in range(n-1, -1, -1):
        #     if i+1 <= n:
        #         dp[i] = dp[i+1]

        #     if i+2 <= n:
        #         dp[i] += dp[i+2]

        # return dp[0]


        # Re-do for the interview
        # [0, 0, 0]
  # idx    0. 1. 2.


        # dp = [0] * (n+1)
        # dp[0] = 1

        # for i in range(1, n+1):
        #     if i-1 >= 0:
        #         dp[i] += dp[i-1]

        #     if i-2 >= 0:
        #         dp[i] += dp[i-2]

        # return dp[n]

        #  n = 3
        # [3, 2, 1, 1]  
        #  0  1  2  3


        #  n = 2
        # [2, 1, 1]
        #  0  1  2 

        # dp[i] = (dp[i+1] + 1) + (dp[i+2] + 1)


        # [0, 1, 2] ; n = 2
        # [0, 1, 3] ; n = 3

        # dp[i] = (dp[i-1] + 1) + (dp[i-2] + 1)

        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            if i-1 >= 0:
                dp[i] += dp[i-1]

            if i-2 >= 0:
                dp[i] += dp[i-2]

        print(dp)
        return dp[-1]