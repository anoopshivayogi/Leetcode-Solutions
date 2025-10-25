class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Solution 0 - Brute force
        # Time - O(n^2)
        # Space - O(1)

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):

        #         if nums[i] == nums[j]:
        #             return True

        # return False


        # Solution 1 - Using set() approach
        # O(n) time
        # O(n) space

        # seen = set()

        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return True
        #     seen.add(nums[i])
        # return False


        # Solution 2 - sort to find duplicates
        # O(nlogn) time
        # O(1) space

        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return True
        # return False


        # Solution 3 - One liner python solution

        # return len(set(nums)) != len(nums)

        # Solution 4 - using freq count
        # Time - O(2n)
        # Space - O(n)

        from collections import Counter
        count = Counter(nums)

        for k, v in count.items():
            if v >= 2:
                return True
        
        return False
