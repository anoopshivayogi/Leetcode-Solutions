from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # Solution 1 - DFS with memoization         

        cache = {}
        
        # @lru_cache(None)
        def dfs(i, target):

            if (i, target) in cache:
                return cache[(i, target)]

            if i == len(nums) and target == 0:
                return 1
            
            if i >= len(nums):
                return 0

            pos = dfs(i+1, target + nums[i])
            neg = dfs(i+1, target + (-nums[i]))

            res = pos + neg

            cache[(i, target)] = res

            return res

        return dfs(0, target)



        # Solution 2 - Dynamic programming bottom up approach


        # n=len(nums)
        # total_sum=sum(nums)
        # s = (target+total_sum)//2
        # target=abs(target)
        # tab = [[0 for i in range(s + 1)] for y in range(n + 1)]

        # if (target>total_sum or (total_sum + target)%2 == 1):
        #     return 0
        # else:
        #     # for j in range(1, s+ 1):
        #     #     tab[0][j] = 0

        #     for i in range(n + 1):
        #         tab[i][0] = 1

        #     for i in range(1,n+1):
        #         for j in range(0,s+1):    
        #             if nums[i-1]<=j:
        #                 tab[i][j]=tab[i-1][j-nums[i-1]] + tab[i-1][j]
        #             else:
        #                 tab[i][j]=tab[i-1][j]

        #     return tab[n][s]



        # n = len(nums)
        # t_sum = sum(nums)

        # subset = (target+t_sum) // 2
        # target = abs(target)

        # dp = [[0 for j in range(subset+1)] for i in range(n+1)]

        # if ((t_sum + target) % 2 == 1) or (target > t_sum):
        #     return 0

        # for i in range(n+1):
        #     dp[i][0] = 1

        # for i in range(1, n+1):
        #     for j in range(subset+1):
        #         # if nums[i-1] <= j:
        #         if j-nums[i-1] >= 0:
        #             dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        #         else:
        #             dp[i][j] = dp[i-1][j]

        # return dp[n][subset]
                

        
        # def dfs(i, target):

        #     if target == 0 and i == len(nums):
        #         return 1
            
        #     if target < 0 or i >= len(nums):
        #         return 0

        #     pos = dfs(i + 1, target - (-nums[i]))
        #     neg = dfs(i + 1, target - (nums[i]))

        #     return pos + neg

        # return dfs(0, target)
