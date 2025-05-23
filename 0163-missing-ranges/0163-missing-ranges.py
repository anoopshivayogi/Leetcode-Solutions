class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        # Solution 1 - Array traversing and edge case handling
        # Time - O(n)
        # Space - O(1) or O(n)

        # if not nums:
        #     return [[lower, upper]]

        # res = []

        # if lower != nums[0]:
        #     res.append([lower, nums[0] - 1])

        # for i in range(len(nums) - 1):
        #     if nums[i+1] - nums[i] > 1:
        #         res.append([nums[i] + 1, nums[i+1] - 1])

        # if upper != nums[-1]:
        #     res.append([nums[-1] + 1, upper])
        
        # return res


        # Re-do for the interview
        # Time - O(n)
        # Space - O(1)

        if not nums:  # NOTE: VERY VERY important edge case
            return [[lower, upper]]

        res = []

        if nums[0] != lower:
            res.append([lower, nums[0] - 1])

        for i in range(1, len(nums)):
            if abs(nums[i-1] - nums[i]) > 1:
                res.append([nums[i-1] + 1, nums[i] - 1])

        if nums[-1] != upper:
            res.append([nums[-1] + 1, upper])

        return res