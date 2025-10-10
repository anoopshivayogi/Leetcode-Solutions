class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        


        # arr = [5, 2, -10, -5, 1] k = 3 ; ans = 100


        # dp = [0, 3, -10, -5, 1]


        # Solution 1 - Using dynamic programming 
        # Time - O(n)
        # Space - O(n)

        n = len(energy)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = energy[i] + (dp[i + k] if i + k < n else 0)

        return max(dp)
