class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        # Solution 1 - Using backtracking - trying out all solutions
        # Time - O(2^n)
        # Space - O(n)
        
        max_or = 0

        for n in nums:
            max_or = max_or | n

        res = [0]
        

        def backtrack(i, cur_or):

            if i >= len(nums) and cur_or == max_or:
                res[0] += 1
                return

            if i >= len(nums):
                return 

            backtrack(i+1, cur_or | nums[i])
            backtrack(i+1, cur_or)
                
        backtrack(0, 0)


        return res[0]
