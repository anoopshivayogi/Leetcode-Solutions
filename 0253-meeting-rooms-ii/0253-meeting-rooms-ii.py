class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # start = sorted([x[0] for x in intervals])
        # # start.sort()

        # end = sorted([x[1] for x in intervals])
        # # end.sort()

        # res, count = 0, 0
        # i, j = 0, 0

        # while i < len(intervals):

        #     if start[i] < end[j]:
        #         count += 1
        #         i += 1
        #     else:
        #         count -= 1
        #         j += 1
        #     res = max(res, count)

        # return res


        # Wrong solution 
        # intervals = sorted(intervals, key=lambda x: x[0])
        # print(intervals)
        # n = len(intervals)
        # i = 1
        # res = 1

        # count = 1
        # while i < n:
        #     while i < n and intervals[i-1][1] > intervals[i][0]:
        #         i += 1
        #         count += 1
        #         res = max(res, count)
        #     i += 1
        #     count = 0

        # return res


        # starts = sorted([s[0] for s in intervals])
        # ends = sorted([s[1] for s in intervals])

        # s, e = 0, 0
        # n = len(intervals)
        # count = 0
        # res = 0

        # while s < n:

        #     if starts[s] < ends[e]:
        #         count += 1
        #         s += 1
        #         res = max(res, count)
        #     else:
        #         count -= 1
        #         e += 1

        # return res



        # Intuition

        # 0               30
        #   5   10
        #          15   20
        # 1 2   1   2    1 0   max -> 2

        # Time - O(n)
        # Space - O(1)

        # starts = sorted([s[0] for s in intervals])
        # ends = sorted([e[1] for e in intervals])

        # s, e = 0, 0
        # res, count = 0, 0


        # while s < len(intervals):
        #     if starts[s] < ends[e]:
        #         s += 1
        #         count += 1
        #     else:
        #         e += 1
        #         count -= 1

        #     res = max(count, res)

        # return res


        # Re-do for the interview
        # Time - O(n)
        # Space - O(n) - Timsort in python requires O(n) space in the worst case

        # s, e = 0, 0
        # res, count = 0, 0

        # starts = sorted([interval[0] for interval in intervals])
        # ends = sorted([interval[1] for interval in intervals])

        # while s < len(intervals):
        #     if starts[s] < ends[e]:
        #         s += 1
        #         count += 1
        #     else:
        #         e += 1
        #         count -= 1

        #     res = max(res, count)

        # return res




        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])


        count = 0
        res = 0
        s, e = 0, 0

        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res