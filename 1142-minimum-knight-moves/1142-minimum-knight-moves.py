class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        

        # Solution 1 - Using BFS 
        # Time - O(max(x^2, y^2)) -> Area of circle is pi*r^2/4 because of first quadrant. 
        # Space - O(max(x^2, y^2)) -> Since you'll be storing all the elements in the set in worst case
        # https://www.youtube.com/watch?v=OgPUNRLSp_c
        # https://medium.com/nerd-for-tech/minimum-knight-moves-daily-challenge-may-4499e5217df5


        directions = [(1, 2), (2, 1), (-1, -2), (-2, -1), (2, -1), (1, -2), (-2, 1), (-1, 2)]

        x = abs(x) # NOTE: Shifting to the first quadrant 
        y = abs(y) # NOTE: Shifting to the first quadrant

        q = collections.deque()
        visit = set()
        q.append((0, 0, 0))  # x, y, moves
        visit.add((0, 0))

        while q:
            cur_x, cur_y, cur_mov = q.popleft()

            if cur_x == x and cur_y == y:
                return cur_mov

            for inc_x, inc_y in directions:
                new_r, new_c = cur_x + inc_x, cur_y + inc_y

                if (new_r, new_c) not in visit and -2 <= new_r < x + 2 and -2 <= new_c < y + 2:  # NOTE: Restricting the boundary is very important 
                    q.append((new_r, new_c, cur_mov + 1))
                    visit.add((new_r, new_c))

        return -1  # NOTE: Not Necessary


        # Solution 2 - Using DFS
        # Time - 
        # Space - 