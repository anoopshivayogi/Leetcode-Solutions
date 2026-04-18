class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Solution 1 - 
        # Time - 
        # Space -

        reverse_num = 0
        num = n

        while num:
            digit = num % 10
            num = num // 10
            reverse_num *= 10
            reverse_num += digit

        return abs(reverse_num - n)