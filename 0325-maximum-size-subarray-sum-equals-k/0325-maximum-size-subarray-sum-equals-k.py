class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        

        # [1, -1, 5, -2, 3], k = 3
        #  0.  1. 2.  3. 4
        #             i
        # total = 3
        # seen = {0: -1, 1: 0, 5: 2}
        # total - k = 0


        # Solution 1 - Prefix sum with hashmap
        # Time - O(n)
        # Space - O(n)

        seen = {0: -1}
        cur_sum = 0
        res = 0

        for idx, num in enumerate(nums):
            cur_sum += num

            if (cur_sum - k) in seen:
                res = max(idx - seen[(cur_sum - k)], res)
            
            if cur_sum not in seen:  # Since we want the longest; Don't update it everytime.
                seen[cur_sum] = idx

        return res