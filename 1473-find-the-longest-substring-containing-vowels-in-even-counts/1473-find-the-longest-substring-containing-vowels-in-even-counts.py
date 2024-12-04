class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        # Solution 1 - Using bit-manipulation and HashMap
        # Time - O(n)
        # Space - O(32) = O(1). 5 different characters; hence 2^5 = 32 different states possible


        # d = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        # mapping = collections.defaultdict(int, d)

        # mask = 0
        # res = 0

        # seen = {0: -1}  # NOTE: Check this; Very important step

        # for idx, ch in enumerate(s):
            
        #     # if ch in mapping:
        #     #     mask ^= mapping[ch]

        #     mask ^= mapping[ch]

        #     if mask in seen:
        #         res = max(res , idx - seen[mask])
        #     else:
        #         seen[mask] = idx

        # return res


        # Solution 2 - Optimised -- Without using hashmap 
        # Time - O(n)
        # Space - O(1)


        # vowel_dict = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        # mapping = collections.defaultdict(int, vowel_dict)
        # mask_to_idx = [-2] * 32   # Maximum 32 possible states

        # mask_to_idx[0] = -1  # Because the math works out this way
        # mask = 0
        # res = 0

        # for idx, ch in enumerate(s):
            
        #     mask ^= mapping[ch]

        #     if mask_to_idx[mask] != -2:
        #         res = max(res, idx - mask_to_idx[mask])
        #     else:
        #         mask_to_idx[mask] = idx

        # return res


        # Re-do for the interview
        # Time - O(n)
        # Space - O(n)


        vowel_dict = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        mapping = collections.defaultdict(int, vowel_dict)
        mask = 0
        mask_to_idx = {0: -1} # Zero can be seen below 0th index; below zero index is -1
        res = 0

        for idx, ch in enumerate(s):
            mask ^= mapping[ch]

            if mask in mask_to_idx:
                res = max(res, idx - mask_to_idx[mask])
            else:
                mask_to_idx[mask] = idx

        return res
            


        # NOTE: Similar problem : 

        # 1. https://leetcode.com/problems/continuous-subarray-sum/
        # 2. https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts
        # 3. https://leetcode.com/problems/path-sum-iii/
        # 4. https://leetcode.com/problems/subarray-sum-equals-k