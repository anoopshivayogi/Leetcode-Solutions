class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # Solution 0 - Brute force
        # Time - O(n)
        # Space - O(1)

        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i + 1]:
        #         return i

        # return len(nums) - 1


        # Solution 1 - Using binary search to find the peak element in the array
        # Time - O(logn)
        # Space - O(1)

        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = (l + r) // 2

        #     left_element = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
        #     right_element = nums[mid + 1] if mid + 1 < len(nums) else float('-inf')

        #     if left_element < nums[mid] > right_element:
        #         return mid
        #     elif left_element > nums[mid] > right_element:
        #         r = mid - 1
        #     else:
        #         l = mid + 1


        # Solution 2 - Slightly modified; if you know that the mid number is decreasing than its neighbor then you know which side to go for sure. 
        # Time - O(n)
        # Space - O(n)

        # NOTE: Needing to know that the neighboring element is rising is enough to know that the current number is not the peak; need not check the other side 
        # But if you do the opposite of the above, it would not work.

        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = (l + r) // 2

        #     if mid > 0 and nums[mid - 1] > nums[mid]:
        #         r = mid - 1
        #     elif mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
        #         l = mid + 1
        #     else:
        #         return mid

        #         0. 1. 2. 3
        # nums = [1, 2, 3, 1]
        #               lm  r
        # return 2

        #         0  1. 2. 3  4. 5. 6
        # nums = [1, 2, 1, 3, 5, 6, 4]
        #         l.       m        r
        # 


        # Re-do for the interview
        # Time - O(logn)
        # Space - O(1)

        # NOTE: IMP!!! if there are no duplicates then there has to be a peak 
        # Clarify that there are no duplicates for this problem 

        l, r = 0, len(nums)

        while l <= r:

            mid = (l + r) // 2

            if mid > 0 and nums[mid - 1] > nums[mid]:
                r = mid - 1
            elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                l = mid + 1
            else:
                return mid

        # Tracing 
        # Case 1 : Peak is in the middle case ; peak = 5
        #   0. 1. 2. 3  4  5. 6
        #  [1, 2, 1, 3, 5, 6, 4]
        #               l 
        #                     r
        #                  m
        

        # Case 2: Peak is at the end ; peak = 4
        #   0  1. 2. 3. 4
        #  [5, 1, 2, 3, 4]
        #               l          
        #               r
        #               m

        
        # Case 3: Peak is at the beginning; peak = 5
        #   0  1. 2. 3. 4
        #  [5, 3, 2, 1, 4]
        #   l
        #      r
        #   m