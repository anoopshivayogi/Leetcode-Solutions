class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # Solution 1 - 
        # Time - 
        # Space - 

        len1, len2 = len(str1), len(str2)

        def is_valid(l):
            if len1 % l or len2 % l:
                return False

            f1, f2 = len1 // l, len2 // l

            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2
            

        
        for idx in range(min(len(str1), len(str2)), 0, -1):
            if is_valid(idx):
                return str1[:idx]

        return ""


        # Solution 2 - Using Euclidean formula for calculating gcd
        # Time - O(log(min(str1, str2)))
        # Space - O(1)

        # def gcd(a, b):  # O(log(min(a, b)))

        #     while b > 0:
        #         a, b = b, a % b

        #     return a
        
        # if str1 + str2 != str2 + str1:
        #     return ""

        # max_len = gcd(len(str1), len(str2))

        # return str1[:max_len]