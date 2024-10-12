class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        # count <= k

        # count = 0
        # [1,1,1,0,0,0,1,1,1,1,0] ; k = 2
        #  lr

        # Solution 1 - Sliding Window technique
        # Time - O(n)
        # Space - O(1)

        # l, res = 0, 0
        # count = 0

        # for r in range(len(nums)):
        #     if nums[r] == 0:
        #         count += 1

        #     while count > k:
        #         if nums[l] == 0:
        #             count -= 1
        #         l += 1

        #     res = max(res, r - l + 1)

        # return res


        # Re-do for the interview
        # Time - 
        # Space -

        res = l = count = 0
        

        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1

            if count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res