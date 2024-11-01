class Solution:
    def makeFancyString(self, s: str) -> str:

        # s = "l e e e t c o d e"
        #                      i
        # st = ['l', 'e', 't', 'c', 'o', 'd', 'e']
        #  if st[-1] == cur_char == next_char

        # s = "a a a b a a a a"
        #                    i
        # st = [a, a, b, a, a]
        
        # Solution 1 - Using stack
        # Time - O(n)
        # Space - O(n)

        # st = []

        # for idx, char in enumerate(s):
            
        #     if st and idx + 1 < len(s) and st[-1] == char == s[idx + 1]:
        #         continue

        #     st.append(char)

        # return "".join(st)


        # Solution 2 - Using just a variable to keep track of the previous char
        # Time - O(n)
        # Space - O(1)

        if len(s) < 3:
            return s

        prev = ''
        res = []

        for idx, char in enumerate(s):

            if prev and idx + 1 < len(s) and prev == char == s[idx + 1]:
                continue

            prev = char
            res.append(char)

        return "".join(res)