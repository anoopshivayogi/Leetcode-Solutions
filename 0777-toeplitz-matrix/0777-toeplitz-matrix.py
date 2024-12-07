class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        # Solution 1 - Using Hashmap with r-c trick
        # Time - O(m*n)
        # Space - O(m*n)


        # 0  [[1, 2, 3, 4],
        # 1   [5, 1, 2, 3],
        # 2   [9, 5, 1, 2]]

        #      0  1  2  3


        #  (2, 0)                    =>  2
        #  (1, 0), (2, 1)            =>  1
        #  (0, 0), (1, 1), (2, 2).   =>  0
        #  (0, 1), (1, 2), (2, 3).   => -1
        #  (0, 2), (1, 3).           => -2
        #  (0, 3)                    => -3



        # Number of diagonals formula -> (M + N - 1)
        # https://math.stackexchange.com/questions/2865964/how-to-prove-that-the-number-of-diagonals-of-a-m-times-n-matrix-is-mn-1

        # seen = dict()
        # ROWS, COLS = len(matrix), len(matrix[0])

        # for r in range(ROWS):
        #     for c in range(COLS):

        #         delta = r - c
        #         if delta in seen:
        #             if seen[delta] != matrix[r][c]:
        #                 return False
        #         else:
        #             seen[delta] = matrix[r][c]

        # return True


        # Solution 2 - Without using extra space; Just check if the top-left item of every element is same
        # Time - O(m*n)
        # Space - O(1)


        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):

                if (r - 1) >= 0 and (c - 1) >= 0:
                    if matrix[r - 1][c - 1] != matrix[r][c]:
                        return False

        return True


        # Solution 3 - Simulation - Cracking Faang Solution 
        # https://www.youtube.com/watch?v=47tY6v-kW5Q
        # Time - O(m*n)
        # Space - O(1)


        # ROWS, COLS = len(matrix), len(matrix[0])

        # def is_diagonal_same(r, c):
        #     val = matrix[r][c]

        #     r += 1  # Go to bottom by one
        #     c += 1  # Go to right by one

        #     while r < ROWS and c < COLS:
        #         if matrix[r][c] != val:
        #             return False

        #         r += 1  # Go to bottom by one
        #         c += 1  # Go to right by one

        #     return True


        # # Check from the beginning of every column
        # for c in range(COLS):
        #     if not is_diagonal_same(0, c):
        #         return False

        # # Check from the beginning of every row
        # for r in range(1, ROWS):
        #     if not is_diagonal_same(r, 0):
        #         return False

        # return True

        # NOTE NOTE : Observe how you count the same diagonal twice while doing the above; That is why you had to start from 1 for row
        # This is also the exact reason why you should do M + N - 1. It is the counting numbers theory.