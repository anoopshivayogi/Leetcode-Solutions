# class SeatManager:

    # def __init__(self, n: int):
    #     self.seats = [None] * (n+1)
    #     self.n = n
    #     self.smallest = 1
        

    # def reserve(self) -> int:
    #     # O(n)

    #     self.seats[self.smallest] = self.smallest
    #     temp = self.smallest

    #     for i in range(self.smallest+1, self.n+1):
    #         if self.seats[i] == None:
    #             # self.seats[i] = i
    #             # return i
    #             self.smallest = i
    #             break

    #     return temp



    # def unreserve(self, seatNumber: int) -> None:
    #     # O(1)
        
    #     self.seats[seatNumber] = None
    #     if self.smallest > seatNumber:
    #         self.smallest = seatNumber

        
        

class SeatManager:

    def __init__(self, n: int):
        self.last = 0
        self.pq = []

    def reserve(self) -> int:
        if not self.pq:
            self.last += 1
            return self.last
        return heapq.heappop(self.pq)

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.last:
            self.last -= 1
        else:
            heapq.heappush(self.pq, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)