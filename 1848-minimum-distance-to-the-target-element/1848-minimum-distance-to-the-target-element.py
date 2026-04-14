class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        

        # Solution 1 - Brute Force
        # Time - O(n)
        # Space - O(1)

        # res = len(nums)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         res = min(res, abs(i - start))
        # return res


        # Solution 2 - Two pointers because we just need to find the index with least distance between i and start
        # Time - O(n)
        # Space - O(1)

        i, j = start, start
        delta = 0
        n = len(nums)

        while True:
            if i + delta < n and nums[i + delta] == target:
                return delta

            if i - delta >= 0 and nums[i - delta] == target:
                return delta

            delta += 1
