class Solution:
    def check(self, nums: List[int]) -> bool:
        

        # Solution 1 - Single iteration
        # Time - O(n)
        # Space - O(1)

        count = 1

        for i, num in enumerate(nums):
            if i > 0:
                if nums[i - 1] <= num:
                    continue
                else:
                    count -= 1
                    if count < 0:
                        return False

        if count == 0 and nums[0] < nums[len(nums) - 1]:
            return False
        
        return True


