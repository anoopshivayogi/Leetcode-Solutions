class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        maxCount = 0

        l, r = 0,0

        while l <= r and r < len(s):
            count[s[r]] += 1
            maxf = max(count.values())

            while ((r-l+1) - maxf) > k:
                count[s[l]] -= 1
                l += 1

            maxCount = max(r - l + 1, maxCount)
            r += 1

        return maxCount


        # Solution 1 - sliding window technique 
        # O(n * 26)
        # O(26) space


        # count = {}
        # res = 0
        # l = 0

        # for r in range(len(s)):

        #     count[s[r]] = 1 + count.get(s[r], 0)
        #     maxf = max(count.values())

        #     while (r-l+1) - maxf > k:
        #         count[s[l]] -= 1
        #         l += 1

        #     res = max(res, r-l+1)

        # return res


        # Solution 2 - sliding window improvement
        # O(n) time
        # O(1) space

        # count = {}
        # res = 0
        # l = 0
        # maxf = 0

        # for r in range(len(s)):

        #     count[s[r]] = 1 + count.get(s[r], 0)
        #     maxf = max(maxf, count[s[r]])

        #     while (r-l+1) - maxf > k:
        #         count[s[l]] -= 1
        #         l += 1

        #     res = max(res, r-l+1)

        # return res


        # Re-Do for the interview
        # "AABABBA" k = 1
        # {A: 1, B: 2}

        # freq = collections.defaultdict(int)
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     freq[s[r]] += 1

        #     # max_char = 
        #     # v = freq[max_char]

        #     while l < r and (r - l + 1) - freq[max(freq, key=lambda ky: freq[ky])] > k:
        #         freq[s[l]] -= 1
        #         if freq[s[l]] == 0:
        #             del freq[s[l]]
        #         l += 1

        #     res = max(res, r - l + 1)

        # return res


        # A B A B ; k = 2
        # l     r
        # {A: 2, B: 2} ; max_f = 2
        # res = 1

        # A A B A B B A ; k = 1
        # l       r
        # {A: 3, B: 2} ; max_f = 3.    |  window_size - maxf > k ; if you don't change maxf to a lower value then you'll not be deleting extra; over approximation kind of
        # res = 


        # time: O(2n * m) = O(n * m) when m = 26; O(n)
        # Space: O(m) when m = 26 ; O(1)

        l, res = 0, 0
        freq = collections.defaultdict(int)

        for r in range(len(s)):
            freq[s[r]] += 1
            max_f = freq[max(freq, key=lambda x: freq[x])]
            while l < r and (r - l + 1) - max_f > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            res = max(res, r - l + 1)

        return res
