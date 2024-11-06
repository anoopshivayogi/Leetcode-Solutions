class Solution:
    def minChanges(self, s: str) -> int:
        
        # Solution 1 - 
        # Time - 
        # Space - 


        res = 0

        for i in range(1, len(s), 2):

            if s[i - 1] != s[i]:
                res += 1

        return res

