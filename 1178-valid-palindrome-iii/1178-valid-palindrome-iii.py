class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        # Solution 1 - Using memoisation
        # Time - O(N^2)  # NOTE: Couldn't actually understand this time complexity; l -> n states ; r -> n states and hence O(n^2) total states stored in the cache
        # Space - O(N^2) 

        # def is_palindrome(l, r):

        #     while l < r:
        #         if s[l] != s[r]:
        #             return False

        #         l += 1
        #         r -= 1

        #     return True

        # # cache = {}

        # from functools import cache
        # @cache
        # def helper(l, r, k):

        #     # if (l, r, k) in cache:
        #     #     return cache[(l, r, k)]

        #     if k == 0:
        #         return is_palindrome(l, r)
        #     else:

        #         while l < r:
        #             if s[l] != s[r]:
        #                 # cache[(l, r, k)] = helper(l + 1, r, k - 1) or helper(l, r - 1, k - 1)
        #                 # return cache[(l, r, k)]

        #                 return helper(l + 1, r, k - 1) or helper(l, r - 1, k - 1)

        #             l += 1
        #             r -= 1
        #         # cache[(l, r, k)] = True
        #         return True

        # return helper(0, len(s) - 1, k)


        # Dry-Run 
        #      0 1 2 3 4 5 6
        # s = "a b c d e c a" ; k = 2
        #              l       
        #              r

        # [dfs(2, 5, 1), dfs(4, 4, 0)] -> Recursive call finished with True

        #      0 1 2 3 4 5 6 7
        # s = "a b b a b a b a", k = 1
        #              l             
        #              r

        # [dfs(3, 5, 0)]   -> recursive call finished with True



        # 0 1 2 3 4 5 6
        # a b c d e c a
        #     l r

        # (0, 6, 2)


        # Time - O(n^2) l -> n states ; r -> n states and hence O(n^2) total states stored in the cache
        # Space - O(n^2) states stored in the cache

        cache = {}

        # from functools import cache
        # @cache
        def helper(l, r):
            if (l, r) in cache:
                return cache[(l, r)]

            if l >= r:
                cache[(l, r)] = 0
                return cache[(l, r)]
                # return 0

            if s[l] == s[r]:
                cache[(l, r)] = helper(l + 1, r - 1)
                return cache[(l, r)]
                # return helper(l + 1, r - 1)
            else:
                cache[(l, r)] = 1 + min(helper(l + 1, r), helper(l, r - 1))
                return cache[(l, r)]
                # return 1 + min(helper(l + 1, r), helper(l, r - 1))

        return helper(0, len(s) - 1) <= k


        # Dry-run

        #      0 1 2 3 4 5 6
        # s = "a b c d e c a", k = 2
        #              l
        #              r

        # [helper(2, 5), helper()]
        # cache = {(4, 4, 0), (2, 5, 1), (3, 3, 0)}

        # 0 1 2 3 4 5 6 7
        # a b b a b a b a
        #     l
        #           r

        # [helper(3, 5)]
        # cache = {(3, 5, 0), (2, 4, 0)}
