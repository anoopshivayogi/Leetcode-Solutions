class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1 - optimal solution, shift left pointer when you find a price which is at the floor level
        # O(n) time
        # O(1) space

        # res = 0
        # i, j = 0, 0


        # for i in range(len(prices)):
        #     curr_p = prices[i] - prices[j]
        #     if curr_p > 0:
        #         res = max(res, curr_p)
        #     else:
        #         j = i

        # return res

        # Solution 2 - same logic; shift left pointer all the way to the right when you find a more lower price
        # O(n) time
        # O(1) space

        # Corner case because of r pointing at 1 in intial stage
        # if len(prices) == 1:
        #     return 0

        # res = 0
        # l, r = 0, 1

        # for r in range(1, len(prices)):
        #     if prices[r] < prices[l]:
        #         l = r
        #     else:
        #         res = max(res, prices[r] - prices[l])

        # return res




        # Re-do it for the interview
        # Time - O(n)
        # Space - O(1)

        # res = 0

        # l = 0

        # for r in range(1, len(prices)):
        #     if prices[r] < prices[l]:
        #         l = r
        #     else:
        #         res = max(res, prices[r] - prices[l])

        # return res


        # Re-do for the interview
        # Time - O(n)
        # Space - O(1)

        res = 0
        l = 0

        for r in range(len(prices)):
            if prices[r] <= prices[l]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])

        return res
            