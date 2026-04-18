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
            reverse_num = reverse_num * 10 + digit

        return abs(reverse_num - n)