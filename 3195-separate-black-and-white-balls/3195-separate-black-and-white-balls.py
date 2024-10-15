class Solution:
    def minimumSteps(self, s: str) -> int:
        

        # Solution 1 - Using two pointers
        # Time - O(n)
        # Space - O(1)

        l = 0
        res = 0

        while l < len(s) and s[l] == 0:
            l += 1

        for r in range(l, len(s)):
            if s[r] == "0":
                res += r - l
                l += 1

        return res

        # Dry-run
        #      0 1 2
        # s = "1 0 1"
        #      l
        #                r  
        # res = 1