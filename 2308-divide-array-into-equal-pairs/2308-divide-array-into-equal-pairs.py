class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Solution 0 - Brute force 
        # Time - 
        # Space - 


        freq = Counter(nums)

        for k, v in freq.items():
            if v % 2:
                return False


        return True