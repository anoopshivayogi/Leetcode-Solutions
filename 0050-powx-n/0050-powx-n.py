class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Solution 1 : Brute Force - Times out O(n) times

        # res = 1

        # for i in range(abs(n)):
        #     res *= x

        # if n >= 0:
        #     return res

        # return 1/res



        # Solution 2 - Recursive with divide and conquer
        # Time - O(Log(n))

        # def backTrack(n):
        #     # Handling two base cases
        #     if n == 0:
        #         return 1
        #     if x == 0:
        #         return 0

        #     res = backTrack(n//2)
        #     res *= res
        #     # Handling if n is odd then you need multiple one more x
        #     return x * res if n%2 else res

        # if n >= 0:
        #     return backTrack(abs(n))
        # else:
        #     return 1/backTrack(abs(n))



        # Re-do for the interview
        # Time - O(logn)
        # Space - O(logn)


        # def recursive(n):
        #     if n == 0:
        #         return 1

        #     if x == 0:
        #         return 0

        #     print(n)

        #     res = recursive(n // 2)

        #     res *= res

        #     return res * x if n % 2 else res

        # if n >= 0:
        #     return recursive(n)
        # else:
        #     return 1 / recursive(abs(n))


# [recursive(10), recursive(5), recursive(2), recursive(1), recursive(0)]
#  res = 2 * 2 * (4 * 2) * 2 == 32 * 32 finally will be equal to 1024


        # Re-do for the interview
        # Time - O(logn)
        # Space - O(logn)

        def recursive(n):

            if n == 0:
                return 1
            
            if x == 0:
                return 0

            res = recursive(n // 2)

            res *= res

            return res * x if n % 2 else res


        if n >= 0:
            return recursive(n)
        else:
            return 1 / recursive(abs(n))
