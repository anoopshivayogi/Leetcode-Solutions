class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Intuition - pointer at each word and move it forward - my solution 
        # Time - O(n) - worst case all strings will be equal chars
        # Space - O(1)

        # res = ''

        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i < len(s) and strs[0][i] == s[i]:
        #             continue
        #         else:
        #             return res
        #     res += strs[0][i]

        # return res


        # Solution NeetCode

        # res = ''

        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or strs[0][i] != s[i]:
        #             return res
        #     res += strs[0][i]

        # return res


        # Re-do for the interview
        # Time - O(n) ; where is the maximum char in the words
        # Space - 

        res = ''
        idx = 0

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += strs[0][i]

        return res