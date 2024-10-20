class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:


        # Solution 2 - 
        # Time - 
        # Space - 

        def gcd(a, b):

            while b > 0:
                a, b = b, a % b

            return a

        
        if str1 + str2 != str2 + str1:
            return ""

        max_len = gcd(len(str1), len(str2))

        return str1[:max_len]