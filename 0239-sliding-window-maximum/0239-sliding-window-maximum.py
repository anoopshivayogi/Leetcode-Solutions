class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Solution 0 - brute force 
        # Time complexity - k(n-k) = O(kn)
        # Space - O(k)
        # Number of windows = n-k+1

        # res = []
        # for i in range(len(nums)):

        #     if i >= k-1:
        #         res.append(max(nums[i-k+1:i+1]))

        # return res



        # Solution 1 - using heapq
        # Time - O(n log n)
        # Space - O(n)

        # import heapq

        # if len(nums) < k:
        #     return -1

        # res = []
        # maxH = []

        
        # for r in range(0, len(nums)):

        #     heapq.heappush(maxH, (-nums[r], r))
            
        #     if r >= (k-1):

        #         while r-k+1 > maxH[0][1]:
        #             heapq.heappop(maxH)
                
        #         res.append(-1 * maxH[0][0])

        # return res



        # Solution 2 - using Deque - monotonic decreasing queue
        # Time - O(n)
        # Space - O(k)

        from collections import deque

        q = deque()
        res = []

        for r in range(len(nums)):
            while q and q[len(q)-1][0] < nums[r]:
                q.pop()

            q.append((nums[r], r))

            if r >= (k-1):

                while r-k+1 > q[0][1]:
                    q.popleft()
                
                res.append(q[0][0])

        return res



            







                


        





