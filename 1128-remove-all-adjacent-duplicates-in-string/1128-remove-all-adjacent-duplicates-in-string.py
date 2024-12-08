class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        # Solution 1 - Using Stack
        # Time - O(N)
        # Space - O(N)

        # st = []

        # for c in s:
        #     if st and st[-1] == c:
        #         st.pop()
        #         continue
        #     st.append(c)

        # return ''.join(st)


        # Re-do for the interview
        # Time - O(n)
        # Space - O(n)

        st = []

        for c in s:
            if st and st[-1] == c:
                st.pop()
            else:
                st.append(c)

        return "".join(st)