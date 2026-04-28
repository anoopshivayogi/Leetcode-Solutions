class Solution:
    def tribonacci(self, n: int) -> int:
        
        
        # States = i to track at which number we are at.
        # dp[i] = the number at ith position we are claculating
        
        # Recurrence relation:
        # dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        # Base condition:
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 1
        
        
        # if n < 1:
        #     return 0
        
        # if n <= 2:
        #     return 1
        
        # dp = [0] * (n+1)
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 1
        
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            
            
        # return dp[-1]

        if n == 0:
            return 0

        if n <= 2:
            return 1
    
        n1, n2, n3 = 0, 1, 1
    
        for i in range(n-2):
            temp = n1 + n2 + n3
            n1 = n2
            n2 = n3
            n3 = temp

        return n3


        
        
        
        