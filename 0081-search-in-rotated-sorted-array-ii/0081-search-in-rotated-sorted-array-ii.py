class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        

        # Solution - Using binary search 
        # Time - 
        # Space - 


        l, r = 0, len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if nums[mid] == target:
                return True
                
            elif nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] == nums[l]:
                    l += 1
                else:
                    r -= 1
            
        return False
