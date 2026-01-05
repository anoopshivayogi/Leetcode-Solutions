class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        # Solution 1 - Brute force
        # Time - 
        # Space - 

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