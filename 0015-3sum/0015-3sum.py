class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Learn how to deal with duplicates in this problem.
        # nums.sort()
        # res = []

        # for i in range(len(nums)):
        #     # Dealing with duplicates #1
        #     if i > 0 and nums[i-1] == nums[i]:
        #         continue


        #     l, r = i+1, len(nums)-1

        #     while l < r:
        #         s = nums[l] + nums[r] + nums[i]
        #         if s == 0:
        #             res.append([nums[l], nums[r], nums[i]])
        #             l += 1
        #             # Dealing with duplicates #2
        #             while l < r and nums[l-1] == nums[l]:
        #                 l += 1
        #                 continue
        #         elif s > 0:
        #             r -= 1
        #         elif s < 0:
        #             l += 1

        # return res



        # Re-do for the interview
        # Time - O(nlogn + n^2) since two sum is O(n) and at worst case call it O(n) times hence = O(n^2) and O(nlogn) for sorting
        # Space - O(1) - Ignoring the extra space for timsort - python implementation of sorting

        # [-4, -1, -1, 0, 1, 2]
        #           i  l  r
        # total = 0


        # [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
        #   i          l                                 r
        # total = 0


        # ONE MORE UNIQUE SOLUTION :
        # INSTEAD OF while l - 1, you can use if l - 1


        # res = []
        # nums.sort()

        # for i in range(len(nums)):
        #     l, r = i + 1, len(nums) - 1

        #     if i > 0 and nums[i - 1] == nums[i]:
        #         continue

        #     while l < r:
        #         total = nums[i] + nums[l] + nums[r]

        #         if total == 0:
        #             if l - 1 > i and nums[l - 1] == nums[l]:
        #                 l += 1
        #                 continue
        #             res.append([nums[i], nums[l], nums[r]])
        #             l += 1
        #             # while l < r and nums[l - 1] == nums[l]:
        #             #     l += 1
        #             #     continue
        #         elif total > 0:
        #             r -= 1
        #         else:
        #             l += 1

        # return res


        # res = []
        # nums.sort()

        # for i in range(len(nums)):
        #     left, right = i + 1, len(nums) - 1

        #     if i - 1 >= 0 and nums[i - 1] == nums[i]:
        #         continue

        #     while left < right:
        #         total = nums[left] + nums[right] + nums[i]

        #         if left - 1 > i and left < right and nums[left - 1] == nums[left]: # NOTE: Be mindful and use only if loop here.
        #             left += 1
        #             continue

        #         if total == 0:
        #             res.append([nums[left], nums[right], nums[i]])
        #             left += 1
        #         elif total > 0:
        #             right -= 1
        #         else:
        #             left += 1

        # return res

        res = []
        nums.sort()

        for i in range(len(nums)):

            l, r = i + 1, len(nums) - 1

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            while l < r:

                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1  #NOTE: Increment 'l' in good case; hence you'll also check for duplicate with l and not r

                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                        continue
                    
                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return res
