class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        

        l, r = 0, len(arr) - 1


        while l <= r:

            mid = (l + r) // 2

            if arr[mid] < arr[mid + 1]: # similar to left bisect
                l = mid + 1
            else:
                r = mid - 1

        return l


        # Tracing 
        #. 0. 1. 2. 3
        # [0, 2, 1, 0]
        #     l         
        #  m
        #  r      


        #  0  1.  2. 3
        # [0, 10, 5, 2]
        #     l
        #. r
        #  m