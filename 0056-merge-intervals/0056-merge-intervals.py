class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort()
        # res = [intervals[0]]

        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= res[-1][1]:
        #         res[-1][1] = max(intervals[i][1], res[-1][1])
        #     else:
        #         res.append(intervals[i])

        # return res


        # Re-do for the interview
        # Time - O(nlogn)
        # Space - O(1) or O(n) for timsort in python

        # intervals.sort()
        # res = [intervals[0]]

        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= res[-1][1]:
        #         res[-1][1] = max(res[-1][1], intervals[i][1])
        #     else:
        #         res.append(intervals[i])

        # return res



        # Re-do for the interview
        # Time - 
        # Space - 

        # [[1,3],[2,6],[8,10],[15,18]]
        #   i

        # intervals.sort(key=lambda x: x[0])
        # res = [intervals[0]]

        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= res[-1][1]:
        #         res[-1][1] = max(intervals[i][1], res[-1][1])
        #     else:
        #         res.append(intervals[i])

        # return res

        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):

            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])

        return res
