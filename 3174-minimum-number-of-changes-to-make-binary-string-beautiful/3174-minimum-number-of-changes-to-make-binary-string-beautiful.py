class Solution:
    def minChanges(self, s: str) -> int:
        
        # Solution 1 - Sliding window approach
        # Time - 
        # Space - 

        


        # Solution 2 - Greedy - Single pointer - Realising that we only need to do pairwise comparasion
        # Time - O(n)
        # Space - O(1) 

        res = 0

        for i in range(1, len(s), 2):

            if s[i - 1] != s[i]:
                res += 1

        return res

