from collections import defaultdict
import random

class Solution:

    def __init__(self, nums: List[int]):
        # Solution 1 - using HashMap
        # Time - O(n) 
        # Space - O(n)

        self.indices = defaultdict(list)
        for idx, num in enumerate(nums):
            self.indices[num].append(idx)

        # Solution 2 - Random sampling
        # https://www.youtube.com/watch?v=HXRN8ZfAQOI
        # Time - O(n)
        # Space - O(1)
        # self.nums = nums

    def pick(self, target: int) -> int:
        # Solution 1 
        return random.choice(self.indices[target])

        # Solution 2 - random sampling - TLE out
        # Time - O(n*m); where m is the number of times pick is called and N is the number of array
        # Space - O(1)
        # https://www.youtube.com/watch?v=HXRN8ZfAQOI

        # count = 0
        # pick_idx = None

        # for idx, n in enumerate(self.nums):
        #     if n == target:
        #         count += 1

        #         if count == random.choice(range(1, count+1)):
        #             pick_idx = idx

        # return pick_idx

        # Re-do for the interview
        # Solution 2 - Resorvier sampling
        # Time - O(n*m) where m is the number of times the pick is called and m is the N is the number of array elements
        # Space - O(1)

        # import random

        # pick_idx = None
        # count = 0

        # for idx, num in enumerate(self.nums):
        #     if num == target:
        #         count += 1

        #         if count == random.choice(range(1, count + 1)):
        #             pick_idx = idx

        # return pick_idx


        # Really missing the proof for why it works for the earlier indices. For example for the second value, probability of 1st selection is 1/2. Probability of being selected next is 1/2 * 2/3 = 1/3. Probability of being selected when you have seen 4 values is 1/2*2/3*3/4 = 1/4. This is what makes the explanation make sense


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)