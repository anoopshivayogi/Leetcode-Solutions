class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        

        # Solution - Using binary search 
        # Time - O(n) at worst and O(logn) at best
        # Space - O(1)


        # l, r = 0, len(nums) - 1

        # while l <= r:

        #     mid = l + (r - l) // 2

        #     if nums[mid] == target:
        #         return True
                
        #     elif nums[l] < nums[mid]:
        #         if nums[l] <= target < nums[mid]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     elif nums[mid] < nums[r]:
        #         if nums[mid] < target <= nums[r]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     else:
        #         if nums[mid] == nums[l]:   #NOTE: Extra case not needed
        #             l += 1
        #         else:
        #             r -= 1
            
        # return False


        # l, r = 0, len(nums) - 1

        # while l <= r:

        #     mid = l + (r - l) // 2

        #     if nums[mid] == target:
        #         return True
                
        #     elif nums[l] < nums[mid]:
        #         if nums[l] <= target < nums[mid]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     elif nums[l] > nums[mid]:
        #         if nums[mid] < target <= nums[r]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     else:
        #         l += 1
            
        # return False


        # Compress at the beginning itself.
        # NOTE: One of the best solution out there.

        l, r = 0, len(nums) - 1

        while l <= r and nums[l] == nums[r]:

            if nums[l] == target:
                return True

            l += 1
            r -= 1

        
        while l <= r:
            
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return True

            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False 