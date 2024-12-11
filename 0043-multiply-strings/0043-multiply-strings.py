class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # Solution 1 - Brute Force 

        # return str(int(num1) * int(num2))

        # Solution 2 - Kind of brute force, doesn't work efficiently for big integers

        # if num1 == "0" or num2 == "0":
        #     return "0"

        # res = 0

        # num1 = num1[::-1]
        # num2 = num2[::-1]

        # for i in range(len(num1)):
        #     x = 1
        #     for p in range(i):
        #         x *= 10
        #     for j in range(len(num2)):
        #         y = 1
        #         for q in range(j):
        #             y *= 10
                
        #         res += (x * int(num1[i])) * (y * int(num2[j]))

        # return str(res)


        # Solution 3 - efficient way for multiplying large integers
        
    
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        res_str = ''

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                res[i+j] += digit  # Add the digit directly
                res[i+j+1] += (res[i + j] // 10)  # Take the carry
                res[i+j] = res[i+j] % 10  # Take the value



        # if we multiple 10 * 10 the result will be [0100]; so we need to get rid of the leading zero

        res = res[::-1]  # reverse it back
        beg = 0 # beginning index

        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])
        return "".join(res)

       
    #     1 2 3
    #     4 5 6

    #     7 3 8
    #   6 1 5 *
    # 4 9 2 * *
    # ----------      
    # 5 6 0 8 8
        

        

        
        
        
        