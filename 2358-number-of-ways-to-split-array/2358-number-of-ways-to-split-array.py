class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        

        # Solution 1 - Using Prefix + additional space
        # Time - O(n)
        # Space - O(1)

        temp = [0] * len(nums)
        res = 0

        for idx in range(len(nums) - 2, -1, -1):
            temp[idx] = (nums[idx + 1] + temp[idx + 1])

        # print(nums)

        pre_sum = 0
        for idx in range(len(nums) - 1):
            pre_sum += nums[idx]
            print(pre_sum)
            if pre_sum >= temp[idx]:
             
                res += 1

        return res
