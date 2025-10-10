class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        


        # [5, 2, -10, -5, 1] k = 3 ; ans = 100


        # arr[i] = max(arr[i-k] + arr[i], arr[i])
        # arr[0] = max(arr[-3] + arr[i], arr[0])

        # arr = [5, 2, -10, 0, 3]

        # max(arr)


        # Solution 1 - Using dynamic programming 
        # Time - 
        # Space - 


        # n = len(energy)
        # dp = [0] * n

        # for i in range(n):
        #     if i - k > 0:
        #         dp[i] = max(dp[i - k] + energy[i], dp[i])
        #     else:
        #         dp[i] = energy[i]

        # return max(dp)

        n = len(energy)
        dp = [0] * n
        result = float('-inf')
        for i in range(n - 1, -1, -1):
            dp[i] = energy[i] + (dp[i + k] if i + k < n else 0)
            result = max(result, dp[i])

        return max(dp)

