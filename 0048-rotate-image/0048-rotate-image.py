class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Solution 1 - using 4 pointer approach 

        # l, r = 0, len(matrix) - 1
        
        # while l < r:
        #     t, b = l, r

        #     for i in range(r-l):
                
        #         # save the top left element
        #         topLeft = matrix[t][l+i]

        #         # shift bottom left element
        #         matrix[t][l+i] = matrix[b-i][l]

        #         # shift bottom right element
        #         matrix[b-i][l] = matrix[b][r-i]

        #         # shift top right element
        #         matrix[b][r-i] = matrix[t+i][r]

        #         # put back topLeft element
        #         matrix[t+i][r] = topLeft

        #     l += 1
        #     r -= 1


        
        # Solution 2 - Reversing rows and transpose(internchanging rows and columns)

        # rows, cols = len(matrix), len(matrix[0])
        # t, b = 0, rows-1

        # while t < b:
        #   matrix[t], matrix[b] = matrix[b], matrix[t]
        #   t += 1
        #   b -= 1

        # for i in range(rows):
        #     for j in range(i):
        #         matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
          

        # Solution 3 - Interchanging row elements with column elements (Doesn't work in-place)
        # O(n^2) extra memory 

        # rows, cols = len(matrix), len(matrix[0])
        # n_matrix = [[0 for j in range(cols)] for i in range(rows)]

        # for i in range(rows):
        #     for j in range(cols):
        #         n_matrix[j][cols-i-1] = matrix[i][j]
        
        # matrix = n_matrix
        





        
        # solution using 4 pointers approach
        # Time - 
        # Space - 

        l, r = 0, len(matrix[0]) - 1 # Column indexes
        t, b = 0, len(matrix) - 1 # Row indexes 

        while l < r:

            for i in range(r - l):

                # Save top left item 
                temp = matrix[t][l + i]

                # Swap bottom-left item to top-left item 
                matrix[t][l + i] = matrix[b - i][l]

                # Swap bottom-right to bottom-left 
                matrix[b - i][l] = matrix[b][r - i]

                # Swap top-right to bottom-right
                matrix[b][r - i] = matrix[t + i][r]

                # Swap top-left(temp) to top-right
                matrix[t + i][r] = temp

            t += 1
            l += 1
            b -= 1
            r -= 1
