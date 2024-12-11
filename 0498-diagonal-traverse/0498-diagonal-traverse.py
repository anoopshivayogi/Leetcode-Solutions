class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        # Solution 1 - Using extra space; clever trick to see that elements on the diagonals have same index sum 
        # Time - O(m*n)
        # Space - O(m*n)

        # https://math.stackexchange.com/questions/2865964/how-to-prove-that-the-number-of-diagonals-of-a-m-times-n-matrix-is-mn-1

        # Intution

        #          0. 1. 2
        #   0  # [[1, 2, 3],      Observer that the diagonal (row + col) indexes add upto same number 
        #   1  #  [4, 5, 6],
        #   2  #  [7, 8, 9]]
    
        # For example: arr[0 + 0] = 1    index 0

        #              arr[1 + 0] = 4    index 1
        #              arr[0 + 1] = 2

        #              arr[2 + 0] = 7    index 2
        #              arr[1 + 1] = 5
        #              arr[0 + 2] = 3     

        # All the even integer index sum should be reversed in the answer 

        
        # index_sum = collections.defaultdict(list)
        # ROWS, COLS = len(mat), len(mat[0])
        
        # for r in range(ROWS):
        #     for c in range(COLS):

        #         index_sum[r+c].append(mat[r][c])

        # res = []

        # for i in range(ROWS + COLS - 1):
        #     if i % 2 == 0:
        #         res.extend(index_sum[i][::-1])
        #     else:
        #         res.extend(index_sum[i])

        # return res


        # Solution 2 - Without using extra space - Simulation
        # Time - O(m * n)
        # Space - O(1) - If we are not counting the result array

        # https://math.stackexchange.com/questions/2865964/how-to-prove-that-the-number-of-diagonals-of-a-m-times-n-matrix-is-mn-1


        if not mat:
            return []

        if not mat[0]:
            return []

        res = []

        ROWS, COLS = len(mat), len(mat[0])
        going_up = True
        cur_row, cur_col = 0, 0

        while len(res) != ROWS * COLS:

            if going_up:
                while cur_row >= 0 and cur_col < COLS:  # NOTE: Take care of this condition

                    res.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1

                if cur_col == COLS:  # (-2, -1)
                    cur_row += 2
                    cur_col -= 1
                else:
                    cur_row += 1

                going_up = False

            else:
                while cur_col >= 0 and cur_row < ROWS:  # NOTE: Take care of this condition

                    res.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1

                if cur_row == ROWS:
                    cur_row -= 1
                    cur_col += 2
                else:
                    cur_col += 1

                going_up = True

        return res