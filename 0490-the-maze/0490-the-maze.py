# class Solution:
#     def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

#         # Solution 1 - Using BFS
#         # Time - O(m.n.(m + n))
#         # Space - O(n.n.(m + n))

#         ROWS, COLS = len(maze), len(maze[0])

#         q = collections.deque()
#         visit = set()
#         q.append((start[0], start[1]))
#         visit.add((start[0], start[1]))

#         directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

#         while q:
#             r, c = q.popleft()

#             if r == destination[0] and c == destination[1]:
#                 return True
            
#             for inc_r, inc_c in directions:
                
#                 new_r, new_c = r, c

#                 while 0 <= new_r < ROWS and 0 <= new_c < COLS and maze[r][c] == 0:
#                     new_r += inc_r
#                     new_c += inc_c

#                 new_r -= inc_r
#                 new_c -= inc_c

#                 if (new_r, new_c) not in visit:
#                     visit.add((new_r, new_c))
#                     q.append((new_r, new_c))

#         return False


from typing import List
import collections

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ROWS, COLS = len(maze), len(maze[0])
        
        q = collections.deque()
        visit = set()
        
        # Starting position
        q.append((start[0], start[1]))
        visit.add((start[0], start[1]))
        
        # Possible directions: right, down, up, left
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        while q:
            r, c = q.popleft()
            
            # Check if we reached the destination
            if [r, c] == destination:
                return True
            
            # Explore in each direction
            for inc_r, inc_c in directions:
                new_r, new_c = r, c  # Start from the current position
                
                # Move in the current direction until hitting a wall
                while 0 <= new_r + inc_r < ROWS and 0 <= new_c + inc_c < COLS and maze[new_r + inc_r][new_c + inc_c] == 0:
                    new_r += inc_r
                    new_c += inc_c
                
                # Check if this position is already visited
                if (new_r, new_c) not in visit:
                    visit.add((new_r, new_c))
                    q.append((new_r, new_c))
        
        # No path found to the destination
        return False
