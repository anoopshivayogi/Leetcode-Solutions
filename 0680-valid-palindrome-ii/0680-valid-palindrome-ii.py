class Solution:
    def validPalindrome(self, s: str) -> bool:

        # Solution 1 - Using two pointers and skip one letter from left and right
        # Time - O(n)
        # Space - O(n)
        
        # def is_palindrome(s: str, l: int, r: int) -> bool:

        #     while l < r:
        #         if s[l] != s[r]:
        #             return False

        #         l += 1
        #         r -= 1

        #     return True

        
        # l, r = 0, len(s) - 1

        # while l < r:
        #     if s[l] != s[r]:
                
        #         if is_palindrome(s, l+1, r) or is_palindrome(s, l, r-1):
        #             return True
        #         else:
        #             return False

        #     l += 1
        #     r -= 1

        # return True

        # Re-Do for the interview
        # Time - O(2 * N/2) - at most the is_palindrome will be called twice
        # Space - O(1)

        def is_palindrome(s, l, r):

            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False

            return True

        
        l, r = 0, len(s) - 1

        while l < r:

            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if is_palindrome(s, l+1, r) or is_palindrome(s, l, r-1):
                    return True
                else:
                    return False

        return True


