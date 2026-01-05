class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        # Solution 1 - Brute force
        # n be the length of the array and let C be the range of elements in the array nums, which does not exceed 10^5
        # Time - O(n * sqrt(C))
        # Space - O(1)

        res = 0
        for num in nums:
            divisors = set()

            for i in range(1, num):
                if i*i > num:
                    break
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)

            if len(divisors) == 4:
                res += sum(divisors)
        
        return res