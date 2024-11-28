class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Solution 1 - Brute Force solution. time complexity = O(nlogn) 

        # LEN1 = len(nums1)-1

        # for n in nums2:
        #     nums1[LEN1] = n
        #     LEN1 -= 1

        # nums1.sort()


        # Solution 2 - Using extra memory. time complexity = O(m+n)

        # copynum1 = nums1[:]
        # copynum1 = nums1.copy()
        # copynum1 = list(nums1)
        # copynum1 = list()
        # for n in nums1:
        #     copynum1.append(n)

        # print(copynum1, nums1)
        # print(copynum1 is nums1) # Just why there is a problem when i use append() ??

        # p1, p2 = 0, 0

        # for p in range(m + n):

        #     if p2 >= n or (p1 < m and copynum1[p1] <= nums2[p2]):
        #         nums1[p] = copynum1[p1]
        #         p1 += 1
        #     else:
        #         nums1[p] = nums2[p2]
        #         p2 += 1


        # Solution 3 - O(1) memory and time complexity = O(m+n)


        # p1, p2 = m-1, n-1

        # for i in range(len(nums1)-1, -1, -1):
        #     if p2 < 0:
        #         break
        #     if nums1[p1] >= nums2[p2] and (p1>=0):
        #         nums1[i] = nums1[p1]
        #         p1 -= 1
        #     else:
        #         nums1[i] = nums2[p2]
        #         p2 -= 1




        # temp = [0] * (m+n)
        # i, j, k = 0, 0, 0

        # while i < m and j < n:

        #     if nums1[i] <= nums2[j]:
        #         temp[k] = nums1[i]
        #         k += 1
        #         i += 1
        #     else:
        #         temp[k] = nums2[j]
        #         k += 1
        #         j += 1

        # while i < m:
        #     temp[k] = nums1[i]
        #     i += 1
        #     k += 1

        # while j < n:
        #     temp[k] = nums2[j]
        #     j += 1
        #     k += 1

        # for i, ele in enumerate(temp):
        #     nums1[i] = ele

        # return nums1




        # Very good thinking to solve this problem
        # RE-DO in a brilliant way


        # i, j = m - 1, n - 1
        # k = len(nums1) - 1


        # while k >= 0:

        #     if i >= 0 and j >= 0:

        #         if nums1[i] >= nums2[j]:
        #             nums1[k] = nums1[i]
        #             k -= 1
        #             i -= 1

        #         else:
        #             nums1[k] = nums2[j]
        #             k -= 1
        #             j -= 1

        #     else:

        #         while i >= 0:
        #             nums1[k] = nums1[i]
        #             k -= 1
        #             i -= 1
        #         while j >= 0:
        #             nums1[k] = nums2[j]
        #             k -= 1
        #             j -= 1


        # Re-do Interview
        # Time - O(n)
        # Space - O(1)


        # nums1 = [1, 2, 2, 3, 5, 6] ; m = 3
            #   i               
            #   k
        # nums2 = [2, 5, 6] ; n = 3
            #   j


        i, j, k = m - 1, n - 1, (m + n - 1)

        while k >= 0:
            
            if i >= 0 and j >= 0:
                
                if nums1[i] >= nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                    k -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
                    k -= 1
            else:
                
                while i >= 0 and k >= 0:
                    nums1[k] = nums1[i]
                    i -= 1
                    k -= 1

                while j >= 0 and k >= 0:
                    nums1[k] = nums2[j]
                    j -= 1
                    k -= 1

        

# nums1 = [1, 2, 2, 3, 5, 6], m = 3, nums2 = [2, 5, 6], n = 3
#          ik                               j