class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        # Solution 1 - using stack you can look back as required
        # Time - O(n)
        # Space - O(n)

        # NOTE: edge conditions: What about the value 0 for the asteriods ?
        #       Will it be considered positive or negative ?

        # st = [] 

        # for a in asteroids:
        #     st.append(a)

        #     while len(st) >= 2 and st[-1] < 0 and st[-2] >= 0:
        #         a1 = st.pop()
        #         a2 = st.pop()

        #         if abs(a1) == a2:
        #             continue
        #         else:
        #             if abs(a1) > a2:
        #                 st.append(a1)
        #             else:
        #                 st.append(a2)
        # return st


        # Re-do for the interview
        # Time - O(n)
        # Space - O(n) - If we count the resultant array otherwise O(1)

        st = []

        for num in asteroids:
            st.append(num)

            while len(st) >= 2 and st[-2] >= 0 and st[-1] < 0:
                a1 = st.pop()
                a2 = st.pop()

                if abs(a1) == abs(a2):
                    continue
                else:
                    if abs(a1) > a2:
                        st.append(a1)
                    else:
                        st.append(a2)

        return st