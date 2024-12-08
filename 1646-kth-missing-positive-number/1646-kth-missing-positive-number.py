class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        # Solution 1 - Linear search.
        # Time - O(n)
        # Space - O(1)

        # If the k is less than the first element of the array.

        # if k <= arr[0] - 1:
        #     return k
        # else:
        #     k -= arr[0] - 1

        # for i in range(len(arr) - 1):

        #     cur_missing = arr[i + 1] - arr[i] - 1

        #     if k <= cur_missing:
        #         return arr[i] + k

        #     k -= cur_missing

        # return arr[-1] + k


        # Intuition 
        #           0. 1. 2. 3. 4. 
        # Orignal: [1, 2, 3, 4, 5]; k = 2

        #.        0. 1. 2. 
        # Given: [1, 4, 5] ;   4 - 1 = 3 Numbers missing but since 0th index reduce one more = 2 number missing.

        # Solution 2 - Binary Search
        # Time - O(logn)
        # Space - O(1)


        left, right = 0, len(arr) - 1

        while left <= right:

            mid = (left + right) // 2
            missing_numbers = (arr[mid] - mid - 1)

            if missing_numbers < k:  # Similar to right bisect because the left will be one over the boundary in the last step.
                left = mid + 1
            else:
                right = mid - 1

        return left + k



    #  Why left + k?

    # At the end of the binary search:
    # The array arr contributes left elements (as left is the index just beyond the considered range).

    # This means there are left non-missing numbers contributed by arr up to this point.
    # The remaining k-th missing number will be located after accounting for these left non-missing numbers.


        # Tracing :
        #        0. 1. 2. 3. 4.
        # arr = [2, 3, 4, 7, 11], k = 5
        #                     l           
        #                     m
        #                     r
        # 
        # missing_numbers = 1





        # https://www.youtube.com/watch?v=NObPmjZIh8Y - Not completely helpful but good
        

