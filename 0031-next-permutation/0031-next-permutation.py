class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1 - Coming from last to find a drop and then swaping it with the higest from right and reversing
        # Time - O(2n) 
        # Space - O(1)

        # https://www.youtube.com/watch?v=6qXO72FkqwM - To understand
        # https://www.youtube.com/watch?v=JRgIqugFhTo - For code


        # pivot = -1

        # for i in range(len(nums) - 1, 0, -1):
        #     if nums[i - 1] < nums[i]:
        #         pivot = i - 1
        #         break


        # if pivot < 0:  # Means the number is in Descending order; Already highest permutation possible
        #     nums.reverse()
        #     return

        # swap_idx = len(nums) - 1

        # while nums[swap_idx] <= nums[pivot]:
        #     swap_idx -= 1

        # nums[swap_idx], nums[pivot] = nums[pivot], nums[swap_idx]
        # # print(pivot, nums[pivot + 1:])
        # nums[pivot + 1:] = reversed(nums[pivot + 1:])

        # return

                #  0. 1. 2
        # nums = [1, 3, 2]
        # pivot = 1
        # swap = 2

             #    0. 1. 2
        # nums = [3, 2, 1]
        # pivot = -1
        # reverse it

                # 0. 1. 2
        # nums = [1, 5, 1]
        # pivot = 1
        # swap = 2


        # NOTE: very good example. 
    #.             0.1 2 3 4
        # nums = [ 1 2 3 5 4 ]
        # pivot = 2
        # swap = 4

        # res = [1 2 4 3 5]


        # Re-do for the interview
        # Time - 
        # Space - 


        pivot_idx = - 1

        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot_idx = i - 1
                break

        if pivot_idx < 0:
            nums.reverse()
            return

        swap_idx = len(nums) - 1

        while nums[swap_idx] <= nums[pivot_idx]:  # NOTE: == is important cz no point in swapping with same number
            swap_idx -= 1

        nums[swap_idx], nums[pivot_idx] = nums[pivot_idx], nums[swap_idx]
        nums[pivot_idx+1: ] = reversed(nums[pivot_idx+1:])

        return
        

        # [1, 5, 1].   <= instead of < case for swapping
        #  p  s 
        # [5, 1, 1]