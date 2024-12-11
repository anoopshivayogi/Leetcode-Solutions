from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Solution 1 : using xor ^

        res = 0

        for n in nums:
            res ^= n

        return res
        

        # Solution 2 : using dict 

        # count = Counter(nums)

        # for k, v in count.items():
        #     if count[k] < 2:
        #         return k


        

