class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        # Solution 0 - Brute force
        # Time - O(n^2)
        # Space - O(1)

        #         0. 1. 2. 3
        # nums = [3, 1, 4, 2], p = 6

        # Starting from jth index to the end index compute all subarray sums and check

        # total = sum(nums)
        # if total % p == 0:
        #     return 0

        # res = len(nums)

        # for i in range(len(nums)):
        #     cur_sum = 0
        #     for j in range(i, len(nums)):
        #         cur_sum += nums[j]
        #         if (total - cur_sum) % p == 0:
        #             res = min(res, j - i + 1)

        # return res if res != len(nums) else -1


        # Solution 1 - hashmap
        # Time - 
        # Space - 

        
        seen = {0: -1}
        target = sum(nums) % p

        if target == 0:  # NOTE: Edge condition
            return 0 

        cur_sum = 0
        min_len = len(nums)

        for idx, num in enumerate(nums):

            cur_sum = (cur_sum + num) % p

            needed = (cur_sum - target + p) % p  # NOTE: Add p to adjust for negative values 

            if needed in seen:
                min_len = min(min_len, idx - seen[needed])

            seen[cur_sum] = idx  # Replace it with the current found irrespectively to find the minimum len

        
        return -1 if min_len == len(nums) else min_len
