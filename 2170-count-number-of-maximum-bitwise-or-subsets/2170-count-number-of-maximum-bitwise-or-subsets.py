class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        # Solution 1 - Using backtracking - trying out all solutions
        # Time - O(2^n)
        # Space - O(n)
        
        max_or = 0

        for n in nums:
            max_or = max_or | n
        
        def backtrack(i, cur_or):

            if i >= len(nums) and cur_or == max_or:
                return 1

            if i >= len(nums):
                return 0
            
            res = 0

            res += backtrack(i+1, cur_or | nums[i])
            res += backtrack(i+1, cur_or)

            return res
                
        return backtrack(0, 0)
