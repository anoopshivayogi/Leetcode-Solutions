class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Solution 1 - Using intersection knowledge 
        # Time - O(M+N)
        # Space - O(M+N) if we count the resultant array otherwise O(1)

        # p1, p2 = 0, 0
        # res = []

        # while p1 < len(firstList) and p2 < len(secondList):

        #     start1, end1 = firstList[p1][0], firstList[p1][1]
        #     start2, end2 = secondList[p2][0], secondList[p2][1]

        #     start = max(start1, start2)
        #     end = min(end1, end2)

        #     # 1    5                        1.   8                             10   15           1.    8  
        #     #    3    10                            10.  15.           1.   8                       6.    10
             
        #     # start=3;end=5              start=10;end=8              start=10;end=8            start=6;min=8

        #     if start <= end:
        #         res.append([start, end])

        #     if end1 > end2:
        #         p2 += 1
        #     else:
        #         p1 += 1

        # return res


        p_ptr, q_ptr = 0, 0
        res = []

        while p_ptr < len(firstList) and q_ptr < len(secondList):
            start1, end1 = firstList[p_ptr][0], firstList[p_ptr][1]
            start2, end2 = secondList[q_ptr][0], secondList[q_ptr][1]

            start_value = max(start1, start2)
            end_value = min(end1, end2)

            if start_value <= end_value:
                res.append([start_value, end_value])
            
            if end1 > end2:
                q_ptr += 1
            else:
                p_ptr += 1

        return res
        