class MedianFinder:
    # Solution 1 - Using two heaps. Max heap for small and Min Heap for large
    # Time - O(4 logn) = O(logn); Finding meadian is O(1)
    # Space - O(n)

    def __init__(self):
        self.small = []
        self.large = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num) # O(logn)

        if self.small and self.large and -self.small[0] > self.large[0]:  # O(logn)
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # After the adjustments check if the size difference is correct; if not correct it

        if len(self.small) > 1 + len(self.large):    # O(2logn)
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        elif len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)


    def findMedian(self) -> float: # O(1)
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
