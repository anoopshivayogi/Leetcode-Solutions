class Solution:
    # def alphaNumeric(self, s: str) -> str:
    #     res = ''

    #     for c in s:
    #         if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('0') and ord(c) <= ord('9')):
    #             res += c.lower()

    #     return res

    # def isAlphaNumeric(self, c: str) -> bool:
    #     if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('0') and ord(c) <= ord('9')):
    #         return True

    #     return False

            

    def isPalindrome(self, s: str) -> bool:

        # Solution 1 - convert the entire str to alphaNumeric and lower
        # O(n) time
        # O(1) space
        
        # s = self.alphaNumeric(s)

        # i, j = 0, len(s)-1

        # while i < j:
        #     if s[i] == s[j]:
        #         i += 1
        #         j -= 1
        #     else:
        #         return False
        
        # return True


        # Solution 2 - skip the unfavourable chars
        # O(n)
        # O(1) space

        # l, r = 0, len(s)-1


        # while l < r:

        #     while l < r and (not self.isAlphaNumeric(s[l])):
        #         l += 1

        #     while l < r and (not self.isAlphaNumeric(s[r])):
        #         r -= 1

        #     if s[l].lower() == s[r].lower():
        #         l += 1
        #         r -= 1
        #     else:
        #         return False

        # return True


        # def isAlphaNumeric(s):
        #     res = ''

        #     for c in s:
        #         if ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'):
        #             res += c.lower()

        #     return res


        # s = isAlphaNumeric(s)

        # l, r = 0, len(s)-1


        # while l < r:
        #     if s[l] == s[r]:
        #         l += 1 
        #         r -= 1
        #     else:
        #         return False

        # return True




        # Re-DO problem for interview

        # def isAlphaNum(c):
        #     return (ord('z') >= ord(c) >= ord('a')) or (ord('Z') >= ord(c) >= ord('A')) or (ord('9') >= ord(c) >= ord('0'))

        # l, r = 0, len(s)-1

        # while l < r:
        #     if isAlphaNum(s[l]):
        #         if isAlphaNum(s[r]):
        #             left = s[l].lower()
        #             right = s[r].lower()

        #             if left == right:
        #                 l += 1
        #                 r -= 1
        #             else:
        #                 return False
        #         else:
        #             r -= 1
        #     else:
        #         l += 1

        # return True



        # Re-do for the interview
        # Time - O(n)
        # Space - O(1)

        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True
