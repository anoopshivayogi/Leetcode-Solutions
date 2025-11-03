class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        

        # Solution 1 - Single pass
        # Time - O(n)
        # Space - O(1)

        # colors = "a b a a a c", neededTime = [1, 2, 3, 4, 5, 6]
        #                   i                             
        #                                                   i
        # ans = 

        # res = float("inf")

        # cur_count = 1
        # cur_ele = a
        # max_time = 4
        # total_time = 7
        # res = inf

        # different = cur_count, cur_ele, max_time, total_time ; update (res += total - max_time)
        # Same = cur_count, low_time, max_time, total_time


        # not a good way:

        cur_ele = colors[0]
        max_time = neededTime[0]
        total_time = neededTime[0]
        res = 0

        for ele, time in zip(colors[1:], neededTime[1:]):
            if ele == cur_ele:
                total_time += time
                max_time = max(max_time, time)
            else:
                # finalize previous group
                res += total_time - max_time
                # reset for new group
                cur_ele = ele
                total_time = time
                max_time = time

        # finalize last group
        res += total_time - max_time
        return res

        # res = 0
        # total_time = neededTime[0]
        # max_time = neededTime[0]

        # for i in range(1, len(colors)):
        #     if colors[i] == colors[i - 1]:
        #         # Same color → part of same group
        #         total_time += neededTime[i]
        #         max_time = max(max_time, neededTime[i])
        #     else:
        #         # Different color → finalize previous group
        #         res += total_time - max_time
        #         total_time = neededTime[i]
        #         max_time = neededTime[i]

        # # finalize last group
        # res += total_time - max_time
        # return res


