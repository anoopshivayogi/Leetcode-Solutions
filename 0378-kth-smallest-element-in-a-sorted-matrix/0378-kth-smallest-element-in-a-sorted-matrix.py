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

        
        n = len(matrix)
        min_heap = []

        for r in range(min(n, k)):
            min_heap.append((matrix[r][0], r, 0))

        heapq.heapify(min_heap)

        while k > 1:

            cur_min, row, col = heapq.heappop(min_heap)

            if col + 1 < n:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))

            k -= 1

        return min_heap[0][0]


        # Solution 2 - Using binary search
        # Time - 
        # Space - 

