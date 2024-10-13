# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        # Solution 1 - Using Binary Search 
        # https://www.youtube.com/watch?v=z_z2gx1-6dQ
        # Time - O(row * log(col))
        # Space - O(1)

        # ROWS, COLS = binaryMatrix.dimensions()
        # res = float('inf')

        # def search_left_most_one(row):  # O(log(col))
        #     l, r = 0, COLS - 1
        #     res = -1

        #     while l <= r:
        #         mid = (l + r) // 2
        #         if binaryMatrix.get(row, mid):
        #             res = mid
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     return res

        # for r in range(ROWS):   # O(row)
        #     left_most_idx = search_left_most_one(r)
        #     if left_most_idx != -1 and left_most_idx < res:
        #         res = left_most_idx

        # return res if res != float('inf') else -1


        # Solution 2 - Smartest way from top right to bottom left
        # Time - O(row + col) not even O(row * col); We'll always finish looking at either row or col
        # Space - O(1)

        ROWS, COLS = binaryMatrix.dimensions()
        row, col = 0, COLS - 1

        while row < ROWS and col >= 0:
            if binaryMatrix.get(row, col):
                col -= 1
            else:
                row += 1

        return col + 1 if col != COLS - 1 else -1