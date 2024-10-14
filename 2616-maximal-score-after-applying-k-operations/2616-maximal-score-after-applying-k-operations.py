class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        

        # Solution 1 - Using heapq
        # Time - O(klog(n+k))
        # Space - O(n + k)

        res = 0

        for idx in range(len(nums)):
            nums[idx] = -nums[idx]

        import heapq
        import math

        heapq.heapify(nums)

        while k:
            cur_max = -heapq.heappop(nums)
            res += cur_max
            heapq.heappush(nums, -math.ceil(cur_max / 3))
            k -= 1

        return res