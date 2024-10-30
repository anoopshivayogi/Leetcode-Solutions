class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # Solution 0 - Using prefix sum
        # Time - O(n)
        # Space - O(n)

        # window_size = (k * 2) + 1
        # n = len(nums)
        # prefix = [0] * (n + 1)
        # res = [-1] * n

        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + nums[i]

        # for i in range(k, n - k):
        #     left_bound, right_bound = i - k, i + k
        #     sub_array = prefix[right_bound + 1] - prefix[left_bound]
        #     average = sub_array // window_size
        #     res[i] = average

        # return res

        
        # Solution 1 - Using sliding window
        # Time - O(2n)
        # Space - O(1)

        # if k == 0: # NOTE: Edge condition in the interview 
        #     return nums

        # win_count = 0
        # l, r = 0, len(nums) - 1
        # res = [-1] * len(nums)
        # window_size = (k*2) + 1

        # if window_size > len(nums):  # NOTE: Edge condition for the interview 
        #     return res

        # for r in range(len(nums)):
        #     win_count += nums[r]

        #     if r >= (k * 2):
        #         res[l+k] = int(win_count / window_size)
        #         win_count -= nums[l]
        #         l += 1

        # return res



        # Solution 2 - Single pointer solution for fixed window
        # Time - O(n)
        # Space - O(1)

        if k == 0: # NOTE: Edge condition in the interview 
            return nums

        win_count = 0
        r = len(nums) - 1
        res = [-1] * len(nums)
        window_size = (k*2) + 1

        if window_size > len(nums):  # NOTE: Edge condition for the interview 
            return res

        for r in range(len(nums)):
            win_count += nums[r]

            if r >= (k * 2):
                l = r - (k * 2)
                res[l+k] = int(win_count / ((k*2) + 1))
                win_count -= nums[l]

        return res
