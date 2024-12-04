class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Solution 1 - using sliding window technique[wrong solution]
        # This solution doesn't work because of the negative values

        # res = 0
        # l = 0
        # cur_sum = 0

        # for r in range(len(nums)):
        #     cur_sum += nums[r]

        #     while l <= r and cur_sum >= k:
        #         if cur_sum == k:
        #             res += 1
        #         cur_sum -= nums[l]
        #         l += 1

        # return res


        # Solution 2 - using prefix sum + hashmap
        # Time - O(n)
        # Space - O(n)

        # prefix_dict = collections.defaultdict(int)
        # prefix_dict[0] = 1

        # cur_sum = 0
        # res = 0

        # for n in nums:
        #     cur_sum += n
        #     res += prefix_dict[cur_sum - k]
        #     prefix_dict[cur_sum] += 1

        # return res


        # Re-Do for the interview
        # Time - O(n)
        # Space - O(n)
        # Intuition - [1, 2, 3]
        # cur_sum - prefix_sum == k ; cur_sum - k == prefix_sum; if you find any such prefix_sum then add it to result
        # {0: 1, 1: 1, 2: 1, 3: 1}

        # cur_sum = 0
        # prefixes = {0: 1}
        # res = 0

        # for n in nums:
        #     cur_sum += n

        #     if (cur_sum - k) in prefixes:
        #         res += prefixes[cur_sum - k]

        #     prefixes[cur_sum] = 1 + prefixes.get(cur_sum, 0)

        # return res



        # Re-do for the interview
        # Time - O(n)
        # Space - O(n)

        # Dry-Run : 

        # nums = [1, 1, 1], k = 2
        #               ^ 
        # prefix = {1: 1, 0: 1, 2: 1, 3: 1}        
        # total = 3  ; 3-2 = 1
        # res = 2

        # Why total - k ? 
        # total - x = k ; we have some 'x' extra but if we deduct that 'x' extra then it'll be equal to k(IDEA
        # interchangably -> total - k = x ; so if we find x in our prefix subarrays then we can add it to result


        prefixes = collections.defaultdict(int)
        prefixes[0] = 1
        cur_total = 0
        res = 0

        for num in nums:
            cur_total += num

            if cur_total - k in prefixes:
                res += prefixes[cur_total - k]

            prefixes[cur_total] += 1

        return res

        # NOTE: Similar problem : 

        # 1. https://leetcode.com/problems/continuous-subarray-sum/
        # 2. https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts
        # 3. https://leetcode.com/problems/path-sum-iii/
        # 4. https://leetcode.com/problems/subarray-sum-equals-k