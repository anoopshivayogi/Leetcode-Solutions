# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:

        # use int() to truncate towards zero in python

        # Solution 1 - using stack
        # time - O(n)
        # space - O(n)


        # st = []
        # operators = set(["+", "-", "*", "/"])

        # for e in tokens:
        #     if e not in operators:
        #         st.append(e)
        #     else:
        #         right = int(st.pop())
        #         left = int(st.pop())
        #         if e == "+":
        #             st.append(left + right)
        #         elif e == "-":
        #             st.append(left - right)
        #         elif e == "*":
        #             st.append(left * right)
        #         elif e == "/":
        #             st.append(left / right)
                

        # return int(st[-1])


        # Re-Do for the interview

        # st = []
        # symbols = set(["+", "-", "/", "*"])


        # for t in tokens:

        #     if t in symbols:
        #         op2 = int(st.pop())
        #         op1 = int(st.pop())
                
        #         if t == "+":
        #             st.append(op1 + op2)
                
        #         if t == "-":
        #             st.append(op1 - op2)

        #         if t == "*":
        #             st.append(op1 * op2)

        #         if t == "/":
        #             st.append(int(op1 / op2))

        #     else:
        #         st.append(t)


        # return int(st[-1])


        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / float(a)))
            else:
                stack.append(int(c))
        return stack[0]





            


