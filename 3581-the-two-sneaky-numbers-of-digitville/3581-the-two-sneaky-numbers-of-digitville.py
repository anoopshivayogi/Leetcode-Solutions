class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        # Solution 1 - Using set
        # Time - O(n)
        # Space - O(n)

        # seen = set()
        # res = []

        # for n in nums:
        #     if n in seen:
        #         res.append(n)
        #     else:
        #         seen.add(n)

        # return res


        # Solution 1 - Using HashMap
        # Time - O(n)
        # Space - O(n)

        freq = Counter(nums)
        res = []

        for k, v in freq.items():
            if v >= 2:
                res.append(k)

        return res
