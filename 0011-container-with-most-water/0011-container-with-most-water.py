class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Solution 1 - Brute Froce
        # O(n^2) time
        # O(1) space
        
        # res = 0

        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = min(height[i], height[j]) * (j - i)
        #         res = max(res, area)
                
        # return res



        # Solution 2 - two pointer approach 

        # l, r = 0, len(height)-1
        # res = 0

        # while l < r:
        #     area = min(height[r], height[l]) * (r-l)
        #     res = max(area, res)

        #     if height[l] > height[r]:
        #         r -= 1
        #     else:
        #         l += 1

        # return res



        # Analysis
        # [1, 8, 6, 2, 5, 4, 8, 3, 7]
        #  l                       r
        #  total = 1 * 8 = 8


        # Re-do for the interview
        # Time - O(n)
        # Space - O(1)

        # l, r = 0, len(height) - 1
        # res = 0

        # while l < r:
        #     res = max(res, min(height[l], height[r]) * (r - l))
        #     if height[l] <= height[r]:
        #         l += 1
        #     else:
        #         r -= 1

        # return res


        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        

        return res