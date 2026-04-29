class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        # Solution 1 - House robber type DP Approach with twist 
        # Time - O(2^n) before caching to O(2*n) = O(n) but sorting takes O(nlogn)
        # Space - O(n) ; space is occupied by freq and also recursive stack

#         from collections import Counter
#         freq = Counter(nums)

#         nums = list(freq.keys())
#         nums.sort()

#         from functools import cache

#         @cache
#         def dfs(i):
#             if i >= len(nums):
#                 return 0

#             # take it
#             if i + 1 < len(nums) and (nums[i] + 1 == nums[i + 1]):
#                 take = (nums[i] * freq[nums[i]]) + dfs(i + 2)
#             else:
#                 take = (nums[i] * freq[nums[i]]) + dfs(i + 1)

#             # Don't take it
#             not_take = dfs(i + 1)

#             return max(take, not_take)

#         return max(dfs(0), dfs(1))


        # Time - O(unique(nums))
        # Space - O(unique(nums))

        # State = index i to track the current maximum number of points you can earn at the number at index i
        # dp[i] = [max points]
        
        # Recurence relation:
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        # base case
        # Its either dp[0] or dp[1]; you need to decide the condition.
        
        
        # freq = Counter(nums)
        # nums = list(freq.keys())
        # nums.sort()
        
        # if len(nums) == 1:
        #     return nums[0] * freq[nums[0]]
        
        # dp = [0] * len(nums)
        
        # dp[0] = nums[0] * freq[nums[0]]
        
        # if nums[1] - nums[0] == 1:
        #     dp[1] = max(dp[0], nums[1] * freq[nums[1]])
        # else:
        #     dp[1] = dp[0] + (nums[1] * freq[nums[1]])

            
        # for i in range(2, len(nums)):
        #     earn_i = (nums[i] * freq[nums[i]])
        #     if nums[i] - nums[i-1] == 1:
        #         dp[i] = max(dp[i-1], earn_i + dp[i-2])
        #     else:
        #         dp[i] = dp[i-1] + earn_i
            
        # return dp[-1]


        # Non space efficient house robber style
        # Time - O(max(nums))
        # Space - O(max(nums))

        if not nums:
            return 0

        max_num = max(nums)

        # Step 1: Build the earn array
        earn = [0] * (max_num + 1)
        for num in nums:
            earn[num] += num

        # Step 2: Apply House Robber DP
        dp = [0] * (max_num + 1)

        # Base cases
        dp[0] = earn[0]
        dp[1] = max(earn[0], earn[1])

        # Fill DP
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + earn[i])

        return dp[max_num]
            
    
    

        
        
        
