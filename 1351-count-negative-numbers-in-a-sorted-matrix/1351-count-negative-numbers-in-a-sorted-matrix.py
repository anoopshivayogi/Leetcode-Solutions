class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        res = 0
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if grid[r][c] >= 0:
                    break
                res += 1

        return res