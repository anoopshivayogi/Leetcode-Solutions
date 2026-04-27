class Solution:

    def rob(self, nums: List[int]) -> int:

        # Solution 1 - in straight order

        # rob1, rob2 = 0, 0

        # for num in nums:
        #     temp = max(rob1 + num, rob2)
        #     rob1 = rob2
        #     rob2 = temp

        # return rob2


        # Solution 2 - In reverse order

        # rob1, rob2 = 0, 0


        # for num in nums[::-1]:
        #     temp = max(rob1 + num, rob2)
        #     rob1 = rob2
        #     rob2 = temp

        # return rob2



        # Solution 3 - Top down approach 

        # from functools import cache

        # @cache
        # def dfs(i):

        #     if i >= len(nums):
        #         return 0

        #     return max(nums[i]+dfs(i+2), dfs(i+1))

        # return dfs(0)


        # Solution 4 - Bottom up 
        # Time - O(n)
        # Space - O(n)


        # for i in range(len(nums)):
        #     if i-2 >= 0:
        #         nums[i] = max(nums[i-1], nums[i] + nums[i-2])
        #     elif i-1 >= 0:
        #         nums[i] = max(nums[i], nums[i-1])

        # return nums[len(nums)-1]









        # Time - O(n)
        # Space - O(n)

        # @cache
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0

        #     res = max(nums[i] + dfs(i+2), dfs(i+1))

        #     return res

        # return dfs(0)


        # Time - O(n)
        # Space - O(1)

        # if len(nums) == 1:
        #     return nums[0]

        # n = len(nums)

        # for i in range(n):

        #     if i-2 >= 0:
        #         nums[i] = max(nums[i-1], nums[i] + nums[i-2])
        #     elif i-1 >= 0:
        #         nums[i] = max(nums[i-1], nums[i])

        # return nums[n-1]

        # from functools import cache

        # @cache
        # def dfs(i):

        #     if i >= len(nums):
        #         return 0

        #     robbed = nums[i] + dfs(i+2)
        #     not_rob = dfs(i+1)

        #     return max(robbed, not_rob)

        # return dfs(0)


        # Dynamic programming solution 
        # Time - O(n) 
        # Space - O(n)

        # n = len(nums)

        # for i in range(n-1, -1, -1):

        #     if i+2 < n:
        #         nums[i] = max(nums[i], nums[i]+nums[i+2])

        #     if i+1 < n:
        #         nums[i] = max(nums[i], nums[i+1])

        # return nums[0]



        # 2026 DP approach thinking in terms of states, recurence relation and then base condition
        # States = just i is enought to track which house you are at.
        # dp[i] = Maximum money robbed up to and including this house.

        # Recurence relation:
        # dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        # Base case (By default we can tell; without depending on any other previous states)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # Time - O(n)
        # Space - O(n)


        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            
        return dp[-1]



















