class Solution:
    def myAtoi(self, s: str) -> int:
        
        # Solution 1 - Scanning characters from left to right
        # Time - O(n)
        # Space - O(1)

        # Build the solution by asking a lot of questions to the interviewer 
        # Will there always be a sign and will there only be one sign ? Can there be more than one sign ?
        # '-+12' => 0   (another sign after one sign is considered as non-digit character)
        # ' 12   4' => 12   (only the leading whitespaces are removed) ; Another space after the digits is considered non-digit character and everything after it will be ignored.


        # NOTE : Notice that cases 1 and 2 are similar for overflow and underflow. The only difference is case 3: for overflow, we can append any digit between 0 and 7, but for underflow, we can append any digit between 0 and 8.


        # sign = 1
        # res = 0
        # i = 0
        # n = len(s)

        # INT_MAX = 2 ** 31 - 1
        # INT_MIN = -1 * (2 ** 31)

        # # Skip leading white spaces
        # while i < n and s[i] == " ":
        #     i += 1
        
        # if i < n and s[i] in "+-":
        #     if s[i] == "-":
        #         sign *= -1
        #     i += 1

        # while i < n and s[i] in "0123456789":
        #     if (res > INT_MAX // 10) or (res == INT_MAX // 10 and int(s[i]) > INT_MAX % 10):
        #         return INT_MAX if sign == 1 else INT_MIN

        #     res = res * 10 + int(s[i])
        #     i += 1
        
        # return sign * res


        # Re-do for the interview
        # Time - O(N)
        # Space - O(1)

        sign = 1
        res = 0
        i = 0
        INT_MAX = (2**31) - 1
        INT_MIN = -1 * (2**31)


        while i < len(s) and s[i] == " ":  # Remove leading whitespace
            i += 1
        
        if i < len(s) and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1

        while i < len(s) and s[i] in "0123456789":

            if (res > INT_MAX // 10) or (res == INT_MAX // 10 and int(s[i]) > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + int(s[i])
            i += 1

        return sign * res