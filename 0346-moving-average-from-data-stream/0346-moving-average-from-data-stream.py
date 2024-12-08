class MovingAverage:

    def __init__(self, size: int):
        # Solution 1 - Using double ended queue
        # Time - O(1)
        # Space - O(N); where N is the size of the moving queue

        from collections import deque

        self.n = size
        self.last_n = deque()
        self.window_sum = 0

        # Solution 2 - You can implement circular queue if you want for this solution

    def next(self, val: int) -> float:
        self.last_n.append(val)
        self.window_sum += val

        # [1, 2, 4, 4, 5]
        #          r
        if len(self.last_n) > self.n:
            removed = self.last_n.popleft()
            self.window_sum -= removed

        return self.window_sum / len(self.last_n)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
