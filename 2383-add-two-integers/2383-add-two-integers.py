class Solution:
    def sum(self, num1: int, num2: int) -> int:

        # Solution 1 - Straightforward way
        # Time - O(1)
        # Space - O(1)
        
        # return num1 + num2


        # Solution 2 - Bitwise Manipulation with XOR and AND operator
        # Time - O(log(n)) -- My guess with time complexity
        # Space - O(1)
        
        mask = 0xfff

        while num2:
            carry = num1 & num2
            num1 = (num1 ^ num2) & mask
            num2 = (carry << 1) & mask

        if num1 > (mask >> 1):
            return ~(num1 ^ mask)

        return num1

        # NOTE
        # NOTE: Follow-up https://leetcode.com/problems/sum-of-two-integers/