class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        # Solution 0 - Brute force
        # Time - O(n^2)
        # Space - O(1)

        #         0. 1. 2. 3
        # nums = [3, 1, 4, 2], p = 6

        # Starting from jth index to the end index compute all subarray sums and check

        # total = sum(nums)
        # if total % p == 0:
        #     return 0

        # res = len(nums)

        # for i in range(len(nums)):
        #     cur_sum = 0
        #     for j in range(i, len(nums)):
        #         cur_sum += nums[j]
        #         if (total - cur_sum) % p == 0:
        #             res = min(res, j - i + 1)

        # return res if res != len(nums) else -1


        # Solution 1 - hashmap
        # Time - 
        # Space - 

        n = len(nums)
        total_sum = 0

        # Step 1: Calculate total sum and target remainder
        total_sum = sum(nums) % p

        target = total_sum % p
        if target == 0:
            return 0  # The array is already divisible by p

        # Step 2: Use a dict to track prefix sum mod p
        mod_map = {
            0: -1
        }  # To handle the case where the whole prefix is the answer
        current_sum = 0
        min_len = n

        # Step 3: Iterate over the array
        for i in range(n):
            current_sum = (current_sum + nums[i]) % p

            # Calculate what we need to remove
            needed = (current_sum - target + p) % p

            # If we have seen the needed remainder, we can consider this subarray
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])

            # Store the current remainder and index
            mod_map[current_sum] = i

        # Step 4: Return result
        return -1 if min_len == n else min_len