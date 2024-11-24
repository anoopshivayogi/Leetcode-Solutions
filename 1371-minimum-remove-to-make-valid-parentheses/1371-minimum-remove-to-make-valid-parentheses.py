class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # Intuition 

        # ex1: lee(t))code -> lee(t)code
        # st = ['(']

        # ex2: "a)b(c)d" -> ab(c)d
        # st = ['(']

        # ex3: "(a"
        # st = ['(']


        # Solution 1 - using stack
        # Time - O(2N)
        # Space - O(N)

        # res = []
        # count = 0

        # for c in s:
        #     if c == ")" and count > 0:
        #         count -= 1
        #         res.append(c)
        #     elif c == "(":
        #         count += 1
        #         res.append(c)
        #     elif c != ")":
        #         res.append(c)

        # filtered = []
        # for c in res[::-1]:
        #     if c == "(" and count > 0:
        #         count -= 1
        #         continue
        #     else:
        #         filtered.append(c)

        # return "".join(filtered[::-1])


        res = []

        count = 0


        for c in s:

            if c == "(":
                count += 1
                res.append(c)
            elif c == ")":
                if count > 0:
                    count -=1
                    res.append(c)
            else:
                res.append(c)

        filtered = []

        for c in res[::-1]:
            if c == "(" and count > 0:
                count -= 1
                continue
            else:
                filtered.append(c)

        return "".join(filtered[::-1])




        # s = "l e e ( t ( c ) o ) d e ) "
        #                                i
        # count = 0
        # res = [l, e, e, (, t, (, c, ), o, ), d, e]


        # s = "a ) b ( c ) d"
        #                  i
        # count = 0
        # res = [a, b, (, c, ), d]


        # s = ") ) ( ("
        #            i
        # count = 0
        # res = []



        # Solve this without using a stack.