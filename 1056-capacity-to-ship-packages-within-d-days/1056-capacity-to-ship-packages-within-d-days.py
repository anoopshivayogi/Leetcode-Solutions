class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # Intuition:-

        # weights = [3,2,2,4,1,4] ; days = 3
        # minimum = max(weights) = 4  ; 4 ; 4 ; 6
        # maximum = sum(weights) = 16 ; 9 ; 6 ; 6

        # Solution 1 - Binary search ?
        # Time - 
        # Space - 

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w 
            return ships <= days


        def can_ship(cap):
            ships = 1
            cur_capacity = cap

            for w in weights:
                if cur_capacity - w < 0:
                    ships += 1
                    cur_capacity = cap
                cur_capacity -= w

            return ships <= days


        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            cap = (l + r) // 2

            if can_ship(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        
        return res



        # l, r = max(weights), sum(weights)
        # res = r

        # def canShip(cap):
        #     ships, currCap = 1, cap
        #     for w in weights:
        #         if currCap - w < 0:
        #             ships += 1
        #             currCap = cap
        #         currCap -= w 
        #     return ships <= days


        # while l <= r:
        #     cap = (l + r) // 2

        #     if canShip(cap):
        #         res = min(res, cap)
        #         r = cap - 1
        #     else:
        #         l = cap + 1

        # return res