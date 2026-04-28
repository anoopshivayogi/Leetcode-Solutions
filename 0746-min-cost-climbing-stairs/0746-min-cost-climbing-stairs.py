class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        
        # states = index i is enough to track a particular staircase
        # dp[i] = minimum cost to reach the step without counting the price at that step
        
        # recurrence relation:
        # dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i-2])
        
        # base case:
        # dp[0] = 0
        # dp[1] = 0
        
        # Time = O(n)
        # Space = O(1)
        
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            
        print(dp)
            
        return dp[-1]
        