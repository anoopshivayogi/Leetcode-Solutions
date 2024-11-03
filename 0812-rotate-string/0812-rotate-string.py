class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        

        # Solution 0 - Brute force
        # Time - O(N^2)
        # Space - O(1)

        # if len(s) != len(goal):
        #     return False

        # for i in range(len(s)):
        #     if s[i:] + s[:i] == goal:
        #         return True

        # return False


        # Solution 1 - Using cleaver technqiue
        # Time - O(m * n) for each character in goal you need to check if it matches every character in s+s
        # Space - O(1)

        return len(s) == len(goal) and goal in s + s


        # Solution 2 - KMP string matching algorithm
        # Time - 
        # Space - 

        # NOTE: TODO

        # https://www.youtube.com/watch?v=-bBOKwD3tT4

