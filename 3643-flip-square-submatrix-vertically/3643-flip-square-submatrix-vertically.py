class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        top_x, top_y = x, y
        bottom_x, bottom_y = x+k-1, y

        while top_x < bottom_x:
            for i in range(top_y, top_y+k):
                grid[top_x][i], grid[bottom_x][i] = grid[bottom_x][i], grid[top_x][i]

            top_x += 1
            bottom_x -= 1

        return grid
