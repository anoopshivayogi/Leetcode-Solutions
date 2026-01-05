class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        
        rows, cols = len(matrix), len(matrix[0])
        total_sum = 0
        min_abs_val = float("inf")
        negative_count = 0

        negatives = []
        for r in range(rows):
            for c in range(cols):
                total_sum += abs(matrix[r][c])
                if matrix[r][c] <= 0:
                    negative_count += 1
                min_abs_val = min(min_abs_val, abs(matrix[r][c]))
        
        if negative_count % 2 != 0: # odd number of negatives
            total_sum -= (2 * min_abs_val)
        
        return total_sum


        # [[2,9,3],
        #  [5,4,-4],
        #  [1,7,1]]