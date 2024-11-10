class Solution:
    def getSum(self, a: int, b: int) -> int:

        # Solution 1 - Using bitwise operation and bounding the result
        # Time - O(1) - because each integer contains 32 bits.
        # Space - O(1) - because we don't use any additional data structures.

        mask = 0xffff
        carry = True

        while carry:
            res = a ^ b
            carry = (a & b) << 1
            a, b = res & mask, carry & mask
        
        # A 32-bit signed integer is positive if the 32nd bit is a 0 and is negative if the 32nd bit is a 1. If we divide our mask (0xffffffff) by 2, we will get the binary number 0b0111111111111111111111111111111, which has 31 1's. This number is the greatest value we can have before the 32nd bit becomes a 1. Therefore, if our answer a > mask // 2(mask >> 1), it is negative. Otherwise, it is positive and we can just return a itself. 
        # if res > (mask >> 1): # mask >> 1(31 bits is the highest number we can store in 32 bits)
        #     return ~(res ^ mask)

        max_int = 0x7fff
        if res > max_int:
            return ~(res ^ mask)

        return res

        # NOTE: Basically for the above problem; The overflow is bound to happen for negative numbers because in 2's complement the sign bit is set. 
        # Expansion Beyond 32 Bits: When bitwise operations (like carry << 1) are applied to simulate addition, Python doesn’t automatically restrict this to 32 bits, so if a negative number is encountered, operations like shifting or adding can cause it to grow beyond 32 bits.
        # Example to Illustrate
        # Consider adding -1 and -2:

        # Representation in 32-bit two's complement:
        # -1 is 0xFFFFFFFF
        # -2 is 0xFFFFFFFE
        # After several bitwise shifts during addition, Python will keep increasing the bits to hold larger results (e.g., 0x1FFFFFFFF), while a true 32-bit system would wrap this back to a 32-bit boundary.
        # Using MASK to Restrict to 32 Bits
        # To simulate fixed-width arithmetic, we apply MASK = 0xFFFFFFFF to limit our intermediate and final results to 32 bits:

        # Masking ensures that after each operation, we only keep the lower 32 bits, effectively mimicking the wrap-around behavior.
        # This keeps Python’s unlimited-bit integer from expanding and enforces a 32-bit boundary, so the result stays within the range of -2^31 to 2^31 - 1.

        # In other languages; the 32 bit wrapping is automatically done. but not in python. So whenever you are dealing with negative numbers; You have to do this masking to stay within the limit yourself.


        # Solution 2 - Calculating borrow for the negative numbers addition
        # Time - 
        # Space - 

