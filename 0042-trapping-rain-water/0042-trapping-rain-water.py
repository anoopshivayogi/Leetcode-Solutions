class Solution:
    def trap(self, height: List[int]) -> int:
        # Solution 1 - with extra space 
        # O(n)
        # O(n)

        # l, r = [0] * len(height), [0] * len(height)
        # lMax, rMax = 0, 0
        # res = 0

        # for i in range(len(height)):
        #     l[i] = lMax
        #     if height[i] > lMax:
        #         lMax = height[i]
             
        # for i in range(len(height)-1, -1, -1):
        #     r[i] = rMax
        #     if height[i] > rMax:
        #         rMax = height[i]

        # for i in range(len(height)):
        #     cur = min(l[i], r[i]) - height[i]
        #     if cur > 0:
        #         res += cur
        
        # return res


        # Solution 2 - Improve on space optimization using two pointers approach
        # O(n) time
        # O(1) space  

        # if not height:
        #     return 0

        # l, r = 0, len(height)-1
        # lMax, rMax = height[l], height[r]
        # res = 0

        # while l<r:

        #     if lMax < rMax:
        #         cur = min(lMax, rMax) - height[l]
        #         l += 1
        #         lMax = max(lMax, height[l])
        #     else:
        #         cur = min(lMax, rMax) - height[r]
        #         r -= 1
        #         rMax = max(rMax, height[r])

        #     if cur > 0:
        #         res += cur

        # return res



        # Solution 1 - Re-do for interview
        # Time - O(n)
        # Space - O(n)

        # n = len(height)
        # l_max, r_max = [0]*n, [0]*n

        # cur_max = 0
        # for i in range(n):
        #     l_max[i] = cur_max
        #     cur_max = max(cur_max, height[i])

        # cur_max = 0
        # for i in range(n-1, -1, -1):
        #     r_max[i] = cur_max
        #     cur_max = max(cur_max, height[i])

        # res = 0
        # for i in range(n):
        #     cur = min(l_max[i], r_max[i]) - height[i]
        #     if cur > 0:
        #         res += cur
        # return res



        # Solution 2 - Most Optimised; Minimizing requires only one lowest number
        # Time - O(N)
        # Space - O(1)

        n = len(height)
        l_min_idx, r_min_idx = 0, n - 1
        l_max, r_max = 0, 0
        res = 0

        while l_min_idx < r_min_idx:

            if height[l_min_idx] < height[r_min_idx]:
                cur_water = l_max - height[l_min_idx]
                l_max = max(l_max, height[l_min_idx])
                l_min_idx += 1
            else:
                cur_water = r_max - height[r_min_idx]
                r_max = max(r_max, height[r_min_idx])
                r_min_idx -= 1

            if cur_water > 0:
                res += cur_water

        return res

            