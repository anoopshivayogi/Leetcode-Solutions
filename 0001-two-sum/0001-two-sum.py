class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 0 - Brute force.
        # Time - nC2 = n(n-1)/2 = O(n^2)
        # Space - O(1)

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):

        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # return [-1, -1]



        # Solution 1 - using hashmap. 
        # Time complexity - O(n)
        # Space complexity - O(n)


        # prevSeen = {} # val = index

        # for i, e in enumerate(nums):
        #     if target-e in prevSeen:
        #         return [prevSeen[target-e], i]
        #     prevSeen[e] = i


        # another type of solution -  two pointers
        # time - O(nlogn)
        # space - O(n)

        # temp = []

        # for i, n in enumerate(nums):
        #     temp.append((n, i))

        # nums = temp
        # nums.sort()

        # l, r = 0, len(nums) - 1

        # while l < r:
        #     cur_sum = nums[l][0] + nums[r][0]
        #     if cur_sum == target:
        #         return [nums[l][1], nums[r][1]]

        #     if cur_sum > target:
        #         r -= 1
        #     else:
        #         l += 1


        # seen = {}

        # for i in range(len(nums)):
        #     remaining = target - nums[i]
        #     if remaining in seen:
        #         return [seen[remaining], i]

        #     seen[nums[i]] = i


        # for i in range(len(nums)):
        #     nums[i] = (nums[i], i)

        # nums.sort()

        # l, r = 0, len(nums) - 1

        # while l < r:
        #     s = nums[l][0] + nums[r][0]
        #     if s == target:
        #         return [nums[l][1], nums[r][1]]

        #     elif s > target:
        #         r -= 1
        #     else:
        #         l += 1


        # O(n); O(n)

        # seen = {}   # Ele : index
        # for idx, ele in enumerate(nums):
        #     if target - ele in seen:
        #         return [idx, seen[target - ele]]
        #     seen[ele] = idx

        # return [-1, -1]


        # Soring and two pointers
        # Time - O(nlogn)
        # Space - O(1)

        # for idx, ele in enumerate(nums):
        #     nums[idx] = (ele, idx)

        # nums.sort()

        # l, r = 0, len(nums) - 1

        # while l < r:
        #     total = nums[l][0] + nums[r][0]
        #     if total == target:
        #         return [nums[l][1], nums[r][1]]

        #     if total > target:
        #         r -= 1
        #     else:
        #         l += 1

        # return -1


        # Aug 3rd 

        # Solution
        # [2,7,11,15] ; target = 9
        #    i
        #  {2: 0}
        #  [1, 0]

        # [3,2,4] ; target = 6
        #  i
        #  {3: 0, 2: 1}
        #  [2, 1]


        # seen = {}

        # for idx, num in enumerate(nums):
        #     remaining = target - num
        #     if remaining in seen:
        #         return [seen[remaining], idx]

        #     seen[num] = idx

        # return [-1, -1]


        # Two pointer approach
        # O(nlogn)
        # O(n) -> Timsort in python takes O(n) extra space at the worst case

        # for i in range(len(nums)):
        #     nums[i] = (nums[i], i)

        # nums.sort()

        # l, r = 0, len(nums) - 1

        # while l < r:
        #     total = nums[l][0] + nums[r][0]
        #     if total == target:
        #         return [nums[l][1], nums[r][1]]
        #     elif total > target:
        #         r -= 1
        #     else:
        #         l += 1

        # return [-1, -1]


        # Re-do for the interview
        # Solution 1 - using hashmap to look back
        # Time - O(n)
        # Space - O(n)

        # seen = {}

        # for idx, num in enumerate(nums):

        #     if target - num in seen:
        #         return [idx, seen[target - num]]

        #     seen[num] = idx

        # return [-1, -1]

        # Solution 2 - sorting and looking it up
        # Time - O(logn)
        # Space - O(1)

        for idx in range(len(nums)):
            nums[idx] = (nums[idx], idx)

        nums.sort()
        l, r = 0, len(nums) - 1

        while l < r:

            if nums[l][0] + nums[r][0] == target:
                return [nums[l][1], nums[r][1]]

            if nums[l][0] + nums[r][0] < target:
                l += 1
            else:
                r -= 1

        return [-1, -1]
