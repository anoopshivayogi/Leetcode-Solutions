class Solution:
    def minimumSteps(self, s: str) -> int:

        # 0 -> white
        # 1 -> black
        

        # Solution 1 - Using two pointers
        # Time - O(n)
        # Space - O(1)

        # l = 0  # White position
        # res = 0

        # for r in range(l, len(s)):
        #     if s[r] == "0":
        #         res += r - l
        #         l += 1

        # return res

        # Dry-run
        #      0 1 2
        # s = "1 0 1"
        #      l
        #                r  
        # res = 1


        # 0 -> white
        # 1 -> black

        # Solution 2 - Using only single pointer
        # Time - 
        # Space - 

        blacks = 0
        res = 0

        for char in s:
            if char == "1":
                blacks += 1
            else:
                res += blacks

        return res
