class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Solution 0 - Brute force; using extra space
        # Time - O(n)
        # Space - O(n)

        # res = []

        # for n in nums:
        #     if n != 0:
        #         res.append(n)

        # for n in nums:
        #     if n == 0:
        #         res.append(n)

        # for i in range(len(nums)):
        #     nums[i] = res[i]



        # Solution 1 - Quick Select/Sort style partitioning algorithm
        # Time - O(n)
        # Space - O(1)

        i = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[i], nums[r] = nums[r], nums[i]
                i += 1

        return nums
