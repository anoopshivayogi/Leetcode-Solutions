class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        # Solution 1 - Using BFS
        # Time - O(m.n.(m + n))
        # Space - O(n.n.(m + n))

        ROWS, COLS = len(maze), len(maze[0])

        q = collections.deque()
        visit = set()
        q.append((start[0], start[1]))
        visit.add((start[0], start[1]))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while q:  # O(m.n)
            r, c = q.popleft()

            if r == destination[0] and c == destination[1]:
                return True
            
            for inc_r, inc_c in directions:
                
                new_r, new_c = r + inc_r, c + inc_c

                while 0 <= new_r < ROWS and 0 <= new_c < COLS and maze[new_r][new_c] == 0: # O(m + n) including all 4 directions
                    new_r += inc_r
                    new_c += inc_c

                new_r -= inc_r
                new_c -= inc_c

                if (new_r, new_c) not in visit:
                    visit.add((new_r, new_c))
                    q.append((new_r, new_c))

        return False
