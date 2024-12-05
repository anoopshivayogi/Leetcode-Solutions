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


        # s_freq = collections.Counter(s)
        # res = ''

        # for c in order:
        #     if c in s_freq:
        #         res += c * s_freq[c]
        #     del s_freq[c]

        # for k, v in s_freq.items():
        #     res += k * v

        # return res


        # Follow-up without using hashmap
        # Time - O(n)
        # Space - O(26) = O(1)

        s_freq = [0] * 26

        for c in s:
            s_freq[ord(c) - ord('a')] += 1

        res = ''

        for c in order:
            if s_freq[ord(c) - ord('a')] >= 0:
                res += c * s_freq[ord(c) - ord('a') ]
            s_freq[ord(c) - ord('a')] = 0


        for i in range(len(s_freq)):
            if s_freq[i] >= 0:
                res += chr(ord('a') + i) * s_freq[i]
            
            s_freq[i] = 0

        return res

        # For example:

        # order: "ab"
        # s: "acbbadbba"
        # Output: "aaabbbbcd"

        # Tracing : 

        # s_freq = {a: 3, c: 1, b: 4, d: 1}
        # res = aaabbbbcd



    # Follow-up Question: Why do you use a hash table (or hashmap, dictionary)?
    # A hash table is used to efficiently store and retrieve the relative order of characters 
    # from the `order` string. By mapping each character in `order` to its index, 
    # we can quickly determine the relative precedence of any character in the `s` string during sorting. 
    # This ensures that sorting is done based on the custom order specified.

    # Follow-up Question: What's the time complexity of getting the value of a key in the map (or dictionary)?
    # In Python, the time complexity of retrieving a value by key in a dictionary is O(1) on average 
    # due to hash table implementation, but it can degrade to O(n) in the worst case due to hash collisions.

    # Follow-up Question: In this case, do you think a map (or dictionary) is better than a sequential scan over the order? Why?
    # Yes, a map (or dictionary) is better than a sequential scan over the `order` string because:
    # 1. Efficiency: Using a dictionary provides O(1) average-time lookups for the position of each character in `order`. 
    #    In contrast, a sequential scan of `order` for each character in `s` would take O(m), where `m` is the length of `order`.
    #    - Sorting `s` with sequential scans would be O(n * m), where `n` is the length of `s`.
    #    - Using a map, sorting can be done in O(n * log n) since custom order determination takes O(1) during comparison.
    # 2. Scalability: As the lengths of `order` and `s` grow, the dictionary approach remains scalable, avoiding repeated linear scans.
    # 3. Code Simplicity: A dictionary allows for cleaner and more concise code, eliminating the need for repeated iterations over `order`.

    # Conclusion: A map or dictionary is the optimal choice for implementing custom sorting efficiently.
