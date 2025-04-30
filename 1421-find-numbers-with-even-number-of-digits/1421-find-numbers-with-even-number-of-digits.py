class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        

        # Solution 1 - Easy string manipulation
        # Time - O(m*n) where m is the number of nums and n is the number of digits in each nums
        # Space - O(1)

        res = 0

        for n in nums:
            if len(str(n)) % 2 == 0:
                res += 1
        
        return res



        # Solution 2 - Getting each number and counting the number of digits
        # Time - 
        # Space -