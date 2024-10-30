class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        

        # Solution 1 - Using sliding window
        # Time - O(n)
        # Space - O()


        # win_count = 0
        # l, r = 0, len(nums) - 1
        # res = [-1] * len(nums)


        # for r in range(len(nums)):
        #     win_count += nums[r]

        #     if r >= (k * 2):
        #         res[l+k] = int(win_count / ((k*2) + 1))
        #         win_count -= nums[l]
        #         l += 1

        # return res


        # Solution 2 - Single pointer solution for fixed window
        # Time - O(n)
        # Space - O(1)


        win_count = 0
        r = len(nums) - 1
        res = [-1] * len(nums)

        for r in range(len(nums)):
            win_count += nums[r]

            if r >= (k * 2):
                l = r - (k * 2)
                res[l+k] = int(win_count / ((k*2) + 1))
                win_count -= nums[l]

        return res