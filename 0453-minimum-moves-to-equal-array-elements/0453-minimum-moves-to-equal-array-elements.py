class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        # Think of the last step, adding 1 to all but one element completes the question, instead you can also decrementing 1 from the element which is bigger than others. Assume we want to equal min and max first, we add 1 to min, keep max untouched. But at the meantime, the other n-2 elements are also increased by 1, min has never got "closer" to these n-2 elements. So every step, we are ONLY 1 closer to the final result.

        # 1.    3
        # 1.    2
        # 1.    1


        res = 0
        max_ele = min(nums)

        for n in nums:
            res += (n - max_ele)

        return res
