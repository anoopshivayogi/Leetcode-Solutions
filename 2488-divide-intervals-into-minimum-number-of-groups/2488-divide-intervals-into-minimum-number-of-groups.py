class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        # Solution 1 - 
        # Time - 
        # Space - 
        
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])

        count = 0
        res = 0 

        s, e = 0, 0

        while s < len(intervals):

            if starts[s] <= ends[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1


            res = max(res, count)

        return res