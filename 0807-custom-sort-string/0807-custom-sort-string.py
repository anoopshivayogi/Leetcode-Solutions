class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Solution 0 - brute force
        # Time - O(n * m)
        # Space - O(s) -> only the result array space

        # res = ''

        # for c in order:
        #     count = 0
        #     for ele in s:
        #         if c == ele:
        #             count += 1

        #     res += c * count

        # for c in s:
        #     if c not in order:
        #         res += c

        # return res


        # Solution 2 - Using Custom Sort Comparator
        # we define N as the length of string s, and K as the length of string order.
        # Time - O(nlogn + k); at most the K here is 26. Hence it becomes O(nlogn)
        # Space - O(n) - extra space for timsort()

        # s = sorted(s, key=lambda x: order.find(x) if order.find(x) >= 0 else float("inf"))

        # return "".join(s)


        # Solution 1 - using dictionary
        # Time - O(n) ; where n is the character count in the string 's'
        # Space - O(26) = O(1) ;
        # SPACE -- if we count res then it is O(n)

        # from collections import Counter

        # freq = Counter(s)

        # res = ""

        # for c in order:
        #     if c in freq:
        #         res += c * freq[c]
        #     del freq[c]

        # for k, v in freq.items():
        #     res += k * v

        # return res


        # Re-do for the interview
        # Time - O(n) ; n is the character count in s
        # Space - O(26) = O(1) if we do not count the space for the resultant variable


        s_freq = collections.Counter(s)
        res = ''

        for c in order:
            if c in s_freq:
                res += c * s_freq[c]
            del s_freq[c]

        for k, v in s_freq.items():
            res += k * v

        return res


        # For example:

        # order: "ab"
        # s: "acbbadbba"
        # Output: "aaabbbbcd"

        # Tracing : 

        # s_freq = {a: 3, c: 1, b: 4, d: 1}
        # res = aaabbbbcd

