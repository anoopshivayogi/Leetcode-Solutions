class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        

        # Solution 0 - Efficiently handling in intervals way by sorting
        # Time - 
        # Space - 

        x_points = [(x[0], x[2]) for x in rectangles]
        y_points = [(y[1], y[3]) for y in rectangles]

        x_points.sort()
        y_points.sort()

        def count_non_overlapping(points):
            count = 0 
            prev_end = -1
            for start, end in points:
                if start >= prev_end:
                    count += 1
                prev_end = max(prev_end, end)

            return count

        return max(count_non_overlapping(x_points), count_non_overlapping(y_points)) >= 3