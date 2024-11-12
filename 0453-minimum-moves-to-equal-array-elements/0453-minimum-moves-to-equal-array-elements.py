class Solution:
    def minMoves(self, nums: List[int]) -> int:


        # Solution 1 - Using sorting
        # Intuition - We know the second highest; third highest etc after updating 
        # Time - O(nlogn)
        # Space - O(n) -- in timsort of pythong sort() implementation

        # nums.sort()
        # res = 0

        # for i in range(len(nums) - 1, -1, -1):
        #     res += nums[i] - nums[0]

        # return res

        # Solution 2 - 
        # Time - 
        # Space - 

        moves = 0
        minimum = float("inf")

        for i in range(len(nums)):
            moves += nums[i]
            minimum = min(nums[i], minimum)

        return moves - minimum * len(nums)


        # Solution 3 - Using the intuition that incrementing (n-1) elements is same as decrementing 1 element
        # Time - O(n)
        # Space - O(1)
        
        # Think of the last step, adding 1 to all but one element completes the question, instead you can also decrementing 1 from the element which is bigger than others. Assume we want to equal min and max first, we add 1 to min, keep max untouched. But at the meantime, the other n-2 elements are also increased by 1, min has never got "closer" to these n-2 elements. So every step, we are ONLY 1 closer to the final result.

        # res = 0
        # min_ele = min(nums)

        # for n in nums:
        #     res += (n - min_ele)

        # return res

        # Solution 3 - 