class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        # Solution 2 - using max_seen so far
        # Time - O(n)
        # Space - O(1)

        # max_seen = float('-inf')
        # res = collections.deque()

        # for i in range(len(heights) - 1, -1, -1):
        #     if heights[i] > max_seen:
        #         res.appendleft(i)
        #     max_seen = max(max_seen, heights[i])

        # return res

        # Re-do for the interview
        # Time - O(n)
        # Space - O(1)

        # max_seen = float('-inf')
        # res = collections.deque()

        # for i in range(len(heights)-1, -1, -1):
        #     if heights[i] > max_seen:
        #         res.appendleft(i)
            
        #     max_seen = max(max_seen, heights[i])

        # return res


        # NOTE: Followup : you can only iterate from the left
        # Solution 2 - Using monotonic stack
        # Time - O(n)
        # Space - O(1) if we don't count the output else O(n)

        # st = [4, 3, 1]

        st = []

        for idx, num in enumerate(heights):
            while st and heights[st[-1]] <= num:
                st.pop()

            st.append(idx)

        return st