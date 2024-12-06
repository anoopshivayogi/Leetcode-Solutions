class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # res = []

        # for i in range(len(intervals)):

        #     if newInterval[1] < intervals[i][0]:
        #         res.append(newInterval)
        #         return res + intervals[i:]
        #     elif newInterval[0] > intervals[i][1]:
        #         res.append(intervals[i])
        #     else:
        #         newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # res.append(newInterval)

        # return res



        # Re-Do for the interview
        # Time - O(n)
        # Space - O(1)

        res = []

        for i in range(len(intervals)):

            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)  # I have done the insertion; now time to append rest of the intervals and return
                return res + intervals[i:]
            else:  # overlapping case
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])

        res.append(newInterval)
        return res
