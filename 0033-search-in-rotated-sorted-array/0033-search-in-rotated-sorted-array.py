class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Solution 1 - using binary search based on different cases
        # Time - O(logn)
        # Space - O(1)

        # l, r = 0, len(nums)-1

        # while l <= r:
        #     mid = (l+r) // 2

        #     if nums[mid] == target:
        #         return mid

        #     if nums[mid] >= nums[l]: # Left portion
        #         if nums[l] > target or nums[mid] < target:
        #             l = mid + 1
        #         elif nums[mid] > target:
        #             r = mid - 1
        #     else:                    # Right portion
        #         if nums[mid] > target or nums[r] < target:
        #             r = mid - 1
        #         elif nums[mid] < target:
        #             l = mid + 1

        # return -1



        # Better way to think
        


        l, r = 0, len(nums)-1
        res = -1

        while l <= r:

            mid = (l+r) // 2

            if nums[mid] == target:
                return mid

            elif nums[l] <= nums[mid]: # belongs to the left side
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            elif nums[r] >= nums[mid]: # belongs to the right side
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1






























            


                    
        