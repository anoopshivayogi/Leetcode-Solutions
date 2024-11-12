class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Solution 1 -> Two pointers and finding median
        # Time - O(m + n)
        # Space - O(m + n)

        # m, n = len(nums1), len(nums2)

        # l, r = 0, 0

        # combi = []

        # while l < m and r < n:

        #     if nums1[l] <= nums2[r]:
        #         combi.append(nums1[l])
        #         l += 1
        #     else:
        #         combi.append(nums2[r])
        #         r += 1

        # while l < m:
        #     combi.append(nums1[l])
        #     l += 1

        # while r < n:
        #     combi.append(nums2[r])
        #     r += 1

        
        # mid = (m+n) // 2


        # if (m+n) % 2 == 0:
        #     return (combi[mid-1] + combi[mid]) / 2
        # else:
        #     return combi[ceil(mid)]



        # Solution 2 - using binary search. 
        # Time - log(m + n)
        # Space - O(1)
        # https://www.youtube.com/watch?v=q6IEA26hvXc

        # Intuition:

        # nums1 = [1, 2] ; nums2 = [3, 4, 5] 
        
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1

        while True:

            i = (l + r) // 2
            j = half - i - 2 # NOTE: -2 is for accounting to count starting from 0

            A_left = A[i] if i >= 0 else float('-inf')
            A_right = A[i + 1] if (i + 1) < len(A) else float("inf")
            B_left = B[j] if j >= 0 else float('-inf')
            B_right = B[j + 1] if (j + 1) < len(B) else float("inf")

            if A_left <= B_right and B_left <= A_right:

                if total % 2:  # Odd case
                    return min(A_right, B_right)
                else:   # Even case
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2

            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
