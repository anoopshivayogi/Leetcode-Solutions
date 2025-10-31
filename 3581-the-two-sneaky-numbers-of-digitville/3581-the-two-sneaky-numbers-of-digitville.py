class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        # Solution 1 - Using set
        # Time - O(n)
        # Space - O(n)

        seen = set()
        res = []

        for n in nums:
            if n in seen:
                res.append(n)
            else:
                seen.add(n)

        return res