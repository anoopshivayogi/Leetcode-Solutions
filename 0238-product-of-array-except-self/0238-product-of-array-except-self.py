class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Solution 1 - using extra space
        # O(n) time
        # O(n) space


        # n = len(nums)

        # l, r = [0] * n, [0] * n


        # l[0] = 1

        # for i in range(1, n):
        #     l[i] = l[i-1] * nums[i-1]

        # r[n-1] = 1

        # for i in range(n-2, -1, -1):
        #     r[i] = r[i+1] * nums[i+1]


        # res = []

        # for i in range(n):
        #     res.append(l[i] * r[i])

        # return res


        # Solution 2 - in-place solution - best solution

        # n = len(nums)

        # prev = 1
        # res = [1] * n

        # for i in range(1, n):
        #     cur = prev * nums[i-1]
        #     res[i] = cur
        #     prev = cur


        # post = 1

        # for i in range(n-2, -1, -1):
        #     cur = post * nums[i+1]
        #     res[i] *= cur
        #     post = cur

        # return res


        # Solution 3 - same one as solution 2 but coding logic a bit easier
        # O(n) time
        # O(1) space

        # res = [1] * (len(nums))

        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res



        # Re-do for the interview from here down all the way


        # left = [1] * len(nums)

        # for i in range(1, len(nums)):
        #     left[i] = left[i-1] * nums[i-1]


        # right = [1] * len(nums)

        # for i in range(len(nums)-2, -1, -1):
        #     right[i] = right[i+1] * nums[i+1]


        # res = []

        # for i in range(len(left)):
        #     res.append(left[i] * right[i])

        # return res



    # nums    [1, 2, 3, 4]

    # left    [1, 1, 2, 6]

    # right   [24 ,12, 4, 1]  

    # res     [24, 12, 8, 6]


        res = [1] * len(nums)
        left = 1

        for i in range(len(nums)):
            res[i] *= left
            left *= nums[i]

        right = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
