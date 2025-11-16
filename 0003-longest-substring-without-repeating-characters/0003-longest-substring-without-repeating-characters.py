class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l, r = 0, 0
        # seen = set()
        # maxCount = 0

        # while l<=r and r < len(s):
        #     while s[r] in seen:
        #         seen.remove(s[l])
        #         l += 1
        #     seen.add(s[r])
        #     maxCount = max(maxCount, r-l+1)
        #     r += 1


        # return maxCount

        # l = 0
        # seen = set()
        # res = 0

        # for r in range(len(s)):

        #     while l < r and s[r] in seen:
        #         seen.remove(s[l])
        #         l += 1

        #     seen.add(s[r])

        #     res = max(res, r - l + 1)

        # return res


        # Re-Do for the interview
        # abcabcbb
        # {a: 2, b: 1}
        # Slightly different implementation using set

        # l = 0
        # res = 0
        # seen = collections.defaultdict(int)

        # for r in range(len(s)):
        #     seen[s[r]] += 1

        #     while l < r and seen[s[r]] > 1:
        #         seen[s[l]] -= 1
        #         l += 1

        #     res = max(res, r - l + 1)

        # return res


        # Re-do for the interview
        # Time - O(n)
        # Space - O(n)

        # dry - run.
        # "a b c a b c b b"
        #  l r
        #  {b, c, a}
        #  res = 3

        # seen = set()
        # l, res = 0, 0

        # for r in range(len(s)):

        #     while l < r and s[r] in seen:
        #         seen.remove(s[l])
        #         l += 1

        #     seen.add(s[r])
        #     res = max(res, r - l + 1)

        # return res


        # s = "a b c a b c b b"
        #            i

        # hashmap = {a: 0; b:1; c: 2}
        # Solution - Most optimized - avoiding O(2n) -> O(n)
        # Time - O(n)
        # Space - O(1)

        i = 0
        seen_map = {}
        res = 0

        for j in range(len(s)):
            if s[j] in seen_map:
                i = max(i, seen_map[s[j]]) # This will handle if the duplicate element we've see is within the window.
            
            seen_map[s[j]] = j+1
            res = max(res, j-i+1)

        return res
