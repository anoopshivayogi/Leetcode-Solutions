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
        # Time - 
        # Space - 


        st = []

        for idx, char in enumerate(s):
            
            if st and idx + 1 < len(s) and st[-1] == char == s[idx + 1]:
                continue

            st.append(char)

        return "".join(st)
