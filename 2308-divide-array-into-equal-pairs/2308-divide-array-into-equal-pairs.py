class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Solution 0 - Brute force using hashmap as frequency counter
        # Time - O(n)
        # Space - O(n)

        freq = Counter(nums)

        for k, v in freq.items():
            if v % 2:
                return False

        return True


        # Solution 1 - 