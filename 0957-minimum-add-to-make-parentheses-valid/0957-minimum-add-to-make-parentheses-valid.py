class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        # Solution 1 - Using stack
        # Time - O(n)
        # Space - O(n)

        # st = []

        # for c in s:
        #     if c == ")" and st and st[-1] == "(":
        #         st.pop()
        #     else:
        #         st.append(c)

        # return len(st)


        # Solution 2 - Without using stack
        # Time - O(n)
        # Space - O(1)

        # res = 0  # closing bracket mismatch count (balance < 0)
        # balance = 0  # '(' positive number meaning opening bracket mismatch

        # for c in s:
        #     if c == ")":
        #         balance -= 1
        #         if balance < 0:
        #             balance = 0
        #             res += 1
        #     else:
        #         balance += 1


        # return res + balance

        # return balance


        # Re-do for the interview  
        # Time - O(n)
        # Space - O(1)


        if not s:
            return 0

        count = 0
        res = 0

        for c in s:
            if c == "(":
                count += 1
            else:
                count -= 1

                if count < 0:
                    res += 1
                    count = 0
        
        return res + count
