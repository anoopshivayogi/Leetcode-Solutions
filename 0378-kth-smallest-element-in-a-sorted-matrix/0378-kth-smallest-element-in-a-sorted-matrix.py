class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # Solution 0 - Brute force - using arrays
        # Time - O(n^2)
        # Space - O(n^2)
        # Just put everything in an array and 


        # Solution 1 - Using heap
        # let x be the min(k, n)
        # Time - O(x) + k * O(log(x)) =  at the worst case k == n ; O(n^2 log(x))
        # Space - O(x) -> Heap occupoed by 'x' elements ; O(n^2) if its the last element
        #      0.  1.  2
        # 0  [[1,  5,  9],
        # 1   [10, 11, 13],
        # 2   [12, 13, 15]]

        
        # n = len(matrix)
        # min_heap = []

        # for r in range(min(n, k)):
        #     min_heap.append((matrix[r][0], r, 0))

        # heapq.heapify(min_heap)

        # while k > 1:

        #     cur_min, row, col = heapq.heappop(min_heap)

        #     if col + 1 < n:
        #         heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))

        #     k -= 1

        # return min_heap[0][0]


        # Solution 2 - Using binary search
        # Time - 
        # Space - 

        def get_less_than_equal(mid):
            count = 0

            n = len(matrix)
            smaller, larger = matrix[0][0], matrix[n-1][n-1]
            row, col = n-1, 0 # Start from bottom left

            while row >= 0 and col < n:

                if matrix[row][col] <= mid:
                    smaller = max(smaller, matrix[row][col])
                    col += 1
                    count += row + 1
                else:
                    larger = min(larger, matrix[row][col])
                    row -= 1

            return count, smaller, larger


        n = len(matrix)
        low, high = matrix[0][0], matrix[n-1][n-1]

        while low < high:
            
            mid = (low + high) // 2
            count, smaller, larger = get_less_than_equal(mid)

            if count == k:
                return smaller
            if count < k:
                low = larger
            else:
                high = smaller

        return low


    #       0  1
    # 0   [[1, 2],
    # 1    [1, 3]]

    # k = 1

    # low = 1, high = 1
    # mid = 1
    # count = 2; smaller = 1; larger = 1

    # [1, 1, 2, 3]