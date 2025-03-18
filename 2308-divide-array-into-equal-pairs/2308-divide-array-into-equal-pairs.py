class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Solution 0 - Brute force using hashmap as frequency counter
        # Time - O(n)
        # Space - O(n)

        # freq = Counter(nums)

        # for k, v in freq.items():
        #     if v % 2:
        #         return False

        # return True


        # Solution 1 - Understand why XOR won't work in this case
        # Time - O(n)
        # Space - O(1)

        # Counter Example : 
        # Given the array [1, 2, 4, 7], computing the XOR:
        # 1⊕2⊕4⊕7=0
        # A result of 0 means that each bit position had an even number of 1s. But this doesn't tell us if elements appeared exactly twice.

        # val = nums[0]

        # for ele in nums[1:]:
        #     val ^= ele

        # print(val)

        # return True if (not val) else False

        # Solution 2 - Using sets
        # Time - 
        # Space - 

        unpaired = set()

        for n in nums:
            if n in unpaired:
                unpaired.remove(n)
            else:
                unpaired.add(n)

        return not unpaired