class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        

        # Solution 1 - Using BFS 
        # Time - O(n)
        # Space - O(n)

        # directions = [(1, 2), (2, 1), (2, -1), (1, -2),
        #            (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        directions = [(1, 2), (2, 1), (-1, -2), (-2, -1), (2, -1), (1, -2), (-2, 1), (-1, 2)]

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

                if (new_r, new_c) not in visit:
                    q.append((new_r, new_c, cur_mov + 1))
                    visit.add((new_r, new_c))

        return -1
