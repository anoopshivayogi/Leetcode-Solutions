class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:


        # NOTE : We add {0 : -1} in dict not to handle case where 1st element is divisible by k.
        # We add it to handle case where subarray starting from 0 is divisible by k.
        # For example when k = 6 and nums = [1,2,3,4] and we don't initialize 0, we will get False.

        # Solution 1 - clever trick using Hashmap
        # Time - O(n)
        # Space - O(n)

        # seen = {0: -1}
        # total = 0

        # for idx, num in enumerate(nums):
        #     total += num
        #     remainder = total % k

        #     # if (remainder in seen) and (idx - seen[remainder] >= 2): # NOTE: This is wrong way of writing logic 

        #     if remainder in seen:
        #         if idx - seen[remainder] >= 2:
        #             return True
        #     else:
        #         seen[remainder] = idx

        # return False


        # Re-do for the interview
        # Time - O(n)
        # Space - O(n)

        seen = {0: -1}
        cur_total = 0

        for idx, num in enumerate(nums):
            cur_total += num
            remainder = cur_total % k

            if remainder in seen:
                if idx - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = idx

        return False
        


        # NOTE: Similar problem : 


        # 1. https://leetcode.com/problems/continuous-subarray-sum/
        # 2. https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts
        # 3. https://leetcode.com/problems/path-sum-iii/