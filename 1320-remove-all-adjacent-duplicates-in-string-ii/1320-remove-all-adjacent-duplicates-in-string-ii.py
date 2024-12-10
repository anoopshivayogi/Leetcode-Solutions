class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        # Solution 1 : 

        # st = []

        # for l in s:
        #     if st and st[-1][0] == l:
        #         st[-1][1] += 1
        #     else:
        #         st.append([l, 1])

        #     if st[-1][1] == k:
        #         st.pop()

        # res = ''

        # for i in st:
        #     res += i[0] * i[1]

        # return res


        # Re-do the interview
        # Time - O(n)
        # Space - O(n)


        st = []


        for c in s:
            if st and st[-1][0] == c:
                st[-1][1] += 1
            else:
                st.append([c, 1])

            if st[-1][1] == k:
                st.pop()


        res = ''

        for c, count in st:
            res += c * count

        return res