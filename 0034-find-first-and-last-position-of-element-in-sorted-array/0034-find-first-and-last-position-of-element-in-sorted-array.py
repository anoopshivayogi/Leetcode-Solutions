class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Solution 1 - Two pointers approach
        # Time - O(n)
        # Space - O(1)


        # l, r = 0, len(nums)-1

        # while l < len(nums) and nums[l] != target:
        #     l += 1

        # while r >= 0 and nums[r] != target:
        #     r -= 1

        # if l <= r:
        #     return [l, r]
        # else:
        #     return [-1, -1]



        # Solution 2 - Using Binary search for two times to find left most and right most
        # Time - O(logn)
        # Space - O(1)


        # l, r = 0, len(nums)-1
        # first = -1

        # while l <= r:
        #     mid = (l+r) // 2

        #     if nums[mid] >= target:
        #         if nums[mid] == target:
        #             first = mid
        #         r = mid - 1
        #     else:
        #         l = mid + 1


        # l, r = 0, len(nums)-1
        # last = -1

        # while l <= r:
        #     mid = (l+r) // 2

        #     if nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         if nums[mid] == target:
        #             last = mid
        #         l = mid + 1

        # return [first, last]


        # Solution 1 - Using binary search to find the first and last elemen's position
        # Time - O(logn)
        # Space - O(1)


        def binary_search(l, r, right_bias):

            i = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    i = mid
                    if right_bias:
                        l = mid + 1
                    else:
                        r = mid - 1
            return i


        first = binary_search(0, len(nums) - 1, False)
        last = binary_search(0, len(nums) - 1, True)

        return [first, last]
