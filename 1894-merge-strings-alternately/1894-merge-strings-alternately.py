class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Solution 1 - Using two pointers
        # Time - O(m + n)
        # Space - O(1)


        # res = ''
        # i, j = 0, 0

        # while i < len(word1) and j < len(word2):
        #     res += word1[i]
        #     i += 1

        #     res += word2[j]
        #     j += 1


        # while i < len(word1):
        #     res += word1[i]
        #     i += 1

        # while j < len(word2):
        #     res += word2[j]
        #     j += 1

        # return res


        # Solution 2 - Using single pointer.
        # Time - O(m + n)
        # Space - O(1)

        res = ''

        for i in range(len(word1) + len(word2)):
            if i < len(word1):
                res += word1[i]

            if i < len(word2):
                res += word2[i]

        return res
