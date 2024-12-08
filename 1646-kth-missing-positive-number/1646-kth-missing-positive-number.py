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

            if missing_numbers < k:  # Similar to left shift
                left = mid + 1
            else:
                right = mid - 1

        return left + k


        # Tracing :

        # arr = [2, 3, 4, 7, 11], k = 5

        #       [1, 1, 1, 3, 6]
