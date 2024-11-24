class Solution:
    def calculate(self, s: str) -> int:

        # Solution 1 - Using stack
        # https://www.youtube.com/watch?v=2EErQ25kKE8
        # Time - O(n)
        # Space - O(n)

        # 10 - 4 + 3 * 2 + 10 / 5
        #            i
        # st = [10, -4, 6, 2] ; total = 14
        # cur = 5
        # prev_operator = /

        # NOTE : you can either do if idx == len(s) - 1 or add extra 'any operator' towards the end of s.

        # cur, st, cur_operation = 0, [], '+'
        # i = 0

        # while i < len(s): # This append towards the end can be any operator "+-*/"

        #     if s[i].isdigit():
        #         while i < len(s) and s[i].isdigit():
        #             cur = cur * 10 + int(s[i])
        #             i += 1
        #         i -= 1  # bring back one extra forward

        #         if cur_operation == "+":
        #             st.append(cur)

        #         elif cur_operation == "-":
        #             st.append(-cur)

        #         elif cur_operation == "/":
        #             st.append(int(st.pop() / cur))

        #         elif cur_operation == "*":
        #             st.append(st.pop() * cur)


        #     elif s[i] != " ":
        #         cur_operation = s[i]
            
        #     i += 1
        #     cur = 0

        # return sum(st)

        # NOTE : the reason it wasn't coming out correct was because the question says "The integer division should truncate toward zero." 
        # When you perform integer division, you get the floor which would result in rounding -0.333 to -1 when it should round to 0 based on the description. 
        # int() however rounds towards 0 which is why it works.



        # Solution 2 - Using just variables - NOTE : Constant space solution
        # Time - O(n)
        # Space - O(1)

        # Tracing
        # 10 - 4 + 3 * 2 + 10 / 5
        #                       i
        # cur = 0 ; prev = 2 ; res = 14 ; cur_operation = '/'

        # cur, prev, res = 0, 0, 0
        # cur_operation = "+"
        # i = 0

        # while i < len(s):

        #     if s[i].isdigit():
        #         while i < len(s) and s[i].isdigit():
        #             cur = cur * 10 + int(s[i])
        #             i += 1
        #         i -= 1  # bring back one extra forward

        #         if cur_operation == "+":
        #             res += cur
        #             prev = cur
        #         elif cur_operation == "-":
        #             res -= cur
        #             prev = -cur
        #         elif cur_operation == "/":
        #             res -= prev
        #             res += int(prev / cur)
        #             prev = int(prev / cur)
        #         elif cur_operation == "*":
        #             res -= prev
        #             res += prev * cur
        #             prev = prev * cur

        #     elif s[i] != " ":
        #         cur_operation = s[i]

        #     i += 1
        #     cur = 0

        # return res



        # Tracing 


        # s = "3+2*2"
        #          i

        # cur = 0
        # cur_operation = "*"
        # prev = 4
        # res = 7


        # s = " 3+5 / 2 "
        #             i
        # cur = 0
        # prev = 2
        # cur_operation = "/"
        # res = 5


        # Re-do for the interview
        # Time - O(n)
        # Space - O(1)

        prev, cur, res = 0, 0, 0
        cur_op = "+"
        i = 0

        while i < len(s):

            if s[i].isdigit():

                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1

                i -= 1  # Bring back one extra forward

                if cur_op == "+":
                    res += cur
                    prev = cur

                elif cur_op == "-":
                    res += (-cur)
                    prev = -cur

                elif cur_op == "/":
                    res -= prev
                    res += int(prev / cur)
                    prev = int(prev / cur)

                elif cur_op == "*":
                    res -= prev
                    res += (prev * cur)
                    prev = (prev * cur)

            elif s[i] != " ":
                cur_op = s[i]

            i += 1
            cur = 0
    
        return res
